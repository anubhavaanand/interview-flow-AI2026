"""
Main FastAPI application for interview-flow-AI2026.
Backend API for DSA interview coaching.
"""

import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from prompts import DSA_FEEDBACK_PROMPT

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="interview-flow-AI2026",
    description="DSA Interview Coach API",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize GitHub Models client
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

client = None

if not GITHUB_TOKEN:
    print("⚠️  Warning: GitHub token not set. Set GITHUB_TOKEN environment variable.")
    print("   Run: ./setup-env.sh")
else:
    try:
        client = OpenAI(
            api_key=GITHUB_TOKEN,
            base_url="https://models.inference.ai.azure.com"
        )
        print("✅ GitHub Models client initialized successfully")
    except Exception as e:
        print(f"⚠️  Warning: Failed to initialize GitHub Models client: {e}")

# ============================================================================
# DATA MODELS
# ============================================================================

class Problem(BaseModel):
    """Data model for a DSA problem."""
    id: str
    title: str
    description: str
    constraints: str
    example: str
    topic: str
    function_signature: str

class AnalysisRequest(BaseModel):
    """Data model for code analysis request."""
    code: str
    topic: str

class Feedback(BaseModel):
    """Data model for AI-generated feedback."""
    time_complexity: str
    space_complexity: str
    edge_cases: str
    code_quality: str
    improvement_plan: list[str]

class AnalysisResponse(BaseModel):
    """Data model for analysis endpoint response."""
    success: bool
    feedback: Feedback = None
    error: str = None

# ============================================================================
# HARDCODED PROBLEM DATA
# ============================================================================

HARDCODED_PROBLEM = Problem(
    id="sliding_window_1",
    title="Maximum Sum Subarray of Size K",
    description="Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.",
    constraints="1 <= k <= n, -1000 <= array[i] <= 1000, 1 <= n <= 10^5",
    example="Input: arr = [2, 1, 5, 1, 3, 2], k = 3\nOutput: 9\nExplanation: The subarray [5, 1, 3] has the maximum sum of 9.",
    topic="sliding_window",
    function_signature="def maxSumSubarray(arr, k):\n    \"\"\"\n    Find the maximum sum of a subarray of size k.\n    \n    Args:\n        arr (list[int]): List of integers\n        k (int): Size of the subarray\n    \n    Returns:\n        int: Maximum sum\n    \"\"\"\n    pass"
)

# ============================================================================
# ROUTES
# ============================================================================

@app.get("/", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "message": "interview-flow-AI2026 API is running",
        "version": "0.1.0"
    }

@app.get("/problem", response_model=Problem, tags=["problems"])
async def get_problem():
    """
    Get a DSA problem.
    Currently returns a hardcoded Sliding Window problem.
    """
    return HARDCODED_PROBLEM

@app.post("/analyze", response_model=AnalysisResponse, tags=["analysis"])
async def analyze_code(request: AnalysisRequest):
    """
    Analyze user's code and provide AI-generated feedback.
    
    Args:
        request: AnalysisRequest with code and topic
    
    Returns:
        AnalysisResponse with feedback from Azure OpenAI
    """
    
    # Validate inputs
    if not request.code or not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    if not request.topic or not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    
    # Check if Azure OpenAI is configured
    if not client:
        raise HTTPException(
            status_code=503,
            detail="GitHub token is not configured. Run: ./setup-env.sh"
        )
    
    try:
        # Build prompt
        prompt = DSA_FEEDBACK_PROMPT.format(
            topic=request.topic,
            code=request.code
        )
        
        # Call GitHub Models API
        response = client.chat.completions.create(
            model="gpt-4o",  # GitHub Models provides GPT-4o
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert DSA interview coach. Provide clear, actionable feedback."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        feedback_text = response.choices[0].message.content
        
        # Parse feedback into structured format
        feedback = parse_feedback(feedback_text)
        
        return AnalysisResponse(
            success=True,
            feedback=feedback
        )
    
    except Exception as e:
        # Log error and return response
        print(f"Error calling GitHub Models: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing code: {str(e)}"
        )

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_feedback(feedback_text: str) -> Feedback:
    """
    Parse AI-generated feedback text into structured Feedback model.
    
    Args:
        feedback_text: Raw feedback text from Azure OpenAI
    
    Returns:
        Feedback: Structured feedback object
    """
    
    # For MVP: Simple parsing. In production, use regex or more robust parsing.
    # This is a basic implementation that extracts sections.
    
    sections = {
        "time_complexity": extract_section(feedback_text, "Time Complexity"),
        "space_complexity": extract_section(feedback_text, "Space Complexity"),
        "edge_cases": extract_section(feedback_text, "Edge Cases"),
        "code_quality": extract_section(feedback_text, "Code Quality"),
        "improvement_plan": extract_improvement_plan(feedback_text)
    }
    
    return Feedback(**sections)

def extract_section(text: str, section_name: str) -> str:
    """Extract a section from feedback text."""
    import re
    # Match the section header and capture everything after it until the next section or end
    # Look for next bold section header or numbered list item
    pattern = rf"\*?\*?{section_name}\*?\*?:\s*(.*?)(?=\n+\*\*|\n+\d+\.|\Z)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        result = match.group(1).strip()
        return result
    return f"No {section_name} analysis provided."

def extract_improvement_plan(text: str) -> list[str]:
    """Extract improvement plan steps from feedback text."""
    import re
    plan_section = re.search(r"(?:3\.\s*)?(?:3-Step\s+)?Improvement Plan:?\s*(.*?)(?=\n\n|\Z)", text, re.IGNORECASE | re.DOTALL)
    
    if plan_section:
        plan_text = plan_section.group(1)
        # Extract lines that look like steps
        steps = []
        
        # Try to find numbered steps first (Step 1:, Step 2:, etc.)
        numbered_steps = re.findall(r"(?:Step\s+\d+:|[-•]\s*Step\s+\d+:)\s*(.+?)(?=\n\s*(?:Step\s+\d+:|[-•])|$)", plan_text, re.IGNORECASE | re.DOTALL)
        if numbered_steps:
            steps = [step.strip() for step in numbered_steps if step.strip()]
        else:
            # Fall back to bullet points
            bullet_steps = re.findall(r"[-•]\s*(.+?)(?=\n\s*[-•]|\n\n|$)", plan_text, re.DOTALL)
            steps = [step.strip() for step in bullet_steps if step.strip()]
        
        if steps:
            return steps
    
    return [
        "Review the code for any inefficiencies",
        "Test with edge cases",
        "Optimize for better time/space complexity"
    ]

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
