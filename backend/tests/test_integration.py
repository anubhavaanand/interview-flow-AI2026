"""
Integration tests for interview-flow-AI2026.
Tests the full flow from problem fetching to code analysis.

Run with: pytest tests/test_integration.py -v
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestFullWorkflow:
    """Integration tests for the complete interview workflow."""
    
    def test_complete_interview_flow(self):
        """Test the complete flow: get problem -> analyze code."""
        
        # Step 1: Fetch a problem
        problem_response = client.get("/problem")
        assert problem_response.status_code == 200
        
        problem_data = problem_response.json()
        problem_topic = problem_data["topic"]
        
        # Step 2: Submit code for analysis
        sample_code = """
def maxSumSubarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
        """
        
        analyze_response = client.post("/analyze", json={
            "code": sample_code,
            "topic": problem_topic
        })
        
        # Response should be 200 (with AI) or 503 (without AI configured)
        assert analyze_response.status_code in [200, 503]
        
        if analyze_response.status_code == 200:
            # If AI is configured, validate response structure
            analysis_data = analyze_response.json()
            assert analysis_data["success"] is True
            
            feedback = analysis_data["feedback"]
            assert "time_complexity" in feedback
            assert "space_complexity" in feedback
            assert "edge_cases" in feedback
            assert "code_quality" in feedback
            assert "improvement_plan" in feedback
            assert isinstance(feedback["improvement_plan"], list)
            assert len(feedback["improvement_plan"]) > 0
    
    def test_multiple_analysis_requests(self):
        """Test submitting multiple code samples in sequence."""
        
        code_samples = [
            "def solution1(arr, k):\n    return sum(arr[:k])",
            "def solution2(arr, k):\n    max_sum = 0\n    for i in range(len(arr)-k+1):\n        max_sum = max(max_sum, sum(arr[i:i+k]))\n    return max_sum",
            "def solution3(arr, k):\n    return max([sum(arr[i:i+k]) for i in range(len(arr)-k+1)])"
        ]
        
        for idx, code in enumerate(code_samples):
            response = client.post("/analyze", json={
                "code": code,
                "topic": "sliding_window"
            })
            
            # Should handle all requests (with or without AI)
            assert response.status_code in [200, 503], f"Failed on sample {idx}"


class TestErrorHandling:
    """Integration tests for error scenarios."""
    
    def test_invalid_code_submission(self):
        """Test that invalid code is properly rejected."""
        
        invalid_codes = [
            "",  # Empty
            "   ",  # Whitespace only
            "x",  # Too short
        ]
        
        for code in invalid_codes:
            response = client.post("/analyze", json={
                "code": code,
                "topic": "array"
            })
            assert response.status_code == 422  # Validation error
    
    def test_system_health_check(self):
        """Test that health check always works."""
        response = client.get("/")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "ok"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
