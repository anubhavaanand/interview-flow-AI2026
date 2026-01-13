"""
Main FastAPI application for interview-flow-AI2026.
Backend API for DSA interview coaching with comprehensive logging and validation.
"""

import os
import json
import logging
from datetime import datetime, timedelta
from functools import lru_cache
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator, Field
from dotenv import load_dotenv
from openai import OpenAI
from prompts import DSA_FEEDBACK_PROMPT
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('api.log')
    ]
)
logger = logging.getLogger(__name__)

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Initialize FastAPI app
app = FastAPI(
    title="interview-flow-AI2026",
    description="DSA Interview Coach API with AI-powered feedback",
    version="0.1.0"
)

# Add rate limiter to app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variable validation at startup
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")  # development or production

# Validate environment variables
@app.on_event("startup")
async def validate_environment():
    """Validate required environment variables on startup."""
    if not GITHUB_TOKEN:
        logger.warning("⚠️  GitHub token not configured. API will not be fully functional.")
        logger.warning("   Set GITHUB_TOKEN environment variable or run: ./setup-env.sh")
    else:
        logger.info("✅ GitHub Models client configured successfully")
    
    # Log environment
    logger.info(f"Running in {ENVIRONMENT} mode")
    
    # Warn if running in production without HTTPS
    if ENVIRONMENT == "production":
        logger.info("🔒 Production mode - ensure HTTPS is configured at reverse proxy level")
        logger.info("   Recommended: Use nginx or similar with SSL/TLS certificates")

# Initialize GitHub Models client
client = None

if GITHUB_TOKEN:
    try:
        client = OpenAI(
            api_key=GITHUB_TOKEN,
            base_url="https://models.inference.ai.azure.com"
        )
        logger.info("✅ GitHub Models client initialized successfully")
    except Exception as e:
        logger.error(f"⚠️  Failed to initialize GitHub Models client: {e}")
else:
    logger.warning("⚠️  Warning: GitHub token not set. Set GITHUB_TOKEN environment variable.")

# ============================================================================
# DATA MODELS WITH VALIDATORS
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
    """Data model for code analysis request with validation."""
    code: str = Field(..., min_length=1, max_length=10000)
    topic: str = Field(..., min_length=1, max_length=100)
    
    @field_validator('code')
    @classmethod
    def validate_code(cls, v):
        """Validate and sanitize code input."""
        if not v or not v.strip():
            raise ValueError('Code cannot be empty or whitespace only')
        
        # Basic sanitization - remove null bytes
        v = v.replace('\x00', '')
        
        # Check for minimum code length (at least some content)
        if len(v.strip()) < 5:
            raise ValueError('Code is too short - please write a meaningful solution')
        
        return v
    
    @field_validator('topic')
    @classmethod
    def validate_topic(cls, v):
        """Validate topic input."""
        if not v or not v.strip():
            raise ValueError('Topic cannot be empty')
        
        # Sanitize topic
        v = v.strip().lower()
        
        # Validate against allowed topics
        allowed_topics = ['sliding_window', 'two_pointers', 'dynamic_programming', 
                         'array', 'string', 'tree', 'graph', 'other']
        if v not in allowed_topics:
            logger.warning(f"Topic '{v}' not in standard list, allowing anyway")
        
        return v

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
    """Health check endpoint with detailed status."""
    logger.info("Health check requested")
    return {
        "status": "ok",
        "message": "interview-flow-AI2026 API is running",
        "version": "0.1.0",
        "ai_configured": client is not None,
        "timestamp": datetime.now().isoformat()
    }

# Cache for problem endpoint (simple in-memory cache)
@lru_cache(maxsize=1)
def get_cached_problem():
    """Get cached problem to reduce processing time."""
    logger.info("Fetching problem (cached)")
    return HARDCODED_PROBLEM

@app.get("/problem", response_model=Problem, tags=["problems"])
@limiter.limit("30/minute")  # Rate limit: 30 requests per minute
async def get_problem(request: Request):
    """
    Get a DSA problem.
    Currently returns a hardcoded Sliding Window problem.
    Response is cached for performance.
    """
    logger.info("GET /problem - Problem requested")
    try:
        problem = get_cached_problem()
        logger.info(f"Returning problem: {problem.id}")
        return problem
    except Exception as e:
        logger.error(f"Error fetching problem: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch problem. Please try again later."
        )

@app.post("/analyze", response_model=AnalysisResponse, tags=["analysis"])
@limiter.limit("10/minute")  # Rate limit: 10 analysis requests per minute
async def analyze_code(data: AnalysisRequest, request: Request):
    """
    Analyze user's code and provide AI-generated feedback.
    
    Args:
        data: AnalysisRequest with validated code and topic
        request: FastAPI Request object for logging
    
    Returns:
        AnalysisResponse with feedback from GitHub Models API
    """
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"POST /analyze - Code analysis requested from {client_ip}")
    logger.info(f"Topic: {data.topic}, Code length: {len(data.code)} chars")
    
    # Check if GitHub Models is configured
    if not client:
        logger.error("Analysis requested but GitHub Models client not configured")
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured. Please contact the administrator or set GITHUB_TOKEN environment variable."
        )
    
    try:
        # Build prompt
        prompt = DSA_FEEDBACK_PROMPT.format(
            topic=data.topic,
            code=data.code
        )
        
        logger.info("Calling GitHub Models API for code analysis")
        
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
        logger.info(f"Received feedback from AI (length: {len(feedback_text)} chars)")
        
        # Parse feedback into structured format
        feedback = parse_feedback(feedback_text)
        
        logger.info("Successfully analyzed code and generated feedback")
        
        return AnalysisResponse(
            success=True,
            feedback=feedback
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log detailed error and return user-friendly message
        logger.error(f"Error analyzing code: {type(e).__name__}: {str(e)}", exc_info=True)
        
        # Provide specific error messages based on error type
        if "timeout" in str(e).lower():
            error_msg = "The AI service timed out. Please try again with a shorter code snippet."
        elif "rate" in str(e).lower() or "quota" in str(e).lower():
            error_msg = "Too many requests. Please wait a moment and try again."
        elif "authentication" in str(e).lower() or "unauthorized" in str(e).lower():
            error_msg = "AI service authentication failed. Please contact the administrator."
        else:
            error_msg = f"Failed to analyze code: {str(e)}"
        
        raise HTTPException(
            status_code=500,
            detail=error_msg
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
