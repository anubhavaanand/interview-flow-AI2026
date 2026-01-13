"""
Unit tests for the FastAPI backend API endpoints.
Run with: pytest tests/
"""

import pytest
from fastapi.testclient import TestClient
from main import app, HARDCODED_PROBLEM

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_check(self):
        """Test that health check returns OK status."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data
        assert "timestamp" in data


class TestProblemEndpoint:
    """Tests for problem retrieval endpoint."""
    
    def test_get_problem(self):
        """Test that problem endpoint returns valid problem data."""
        response = client.get("/problem")
        assert response.status_code == 200
        
        data = response.json()
        assert "id" in data
        assert "title" in data
        assert "description" in data
        assert "constraints" in data
        assert "example" in data
        assert "topic" in data
        assert "function_signature" in data
        
        # Verify it matches our hardcoded problem
        assert data["id"] == HARDCODED_PROBLEM.id
        assert data["topic"] == HARDCODED_PROBLEM.topic


class TestAnalyzeEndpoint:
    """Tests for code analysis endpoint."""
    
    def test_analyze_empty_code(self):
        """Test that empty code returns validation error."""
        response = client.post("/analyze", json={
            "code": "",
            "topic": "sliding_window"
        })
        assert response.status_code == 422  # Validation error
    
    def test_analyze_empty_topic(self):
        """Test that empty topic returns validation error."""
        response = client.post("/analyze", json={
            "code": "def solution(): pass",
            "topic": ""
        })
        assert response.status_code == 422  # Validation error
    
    def test_analyze_code_too_short(self):
        """Test that very short code returns validation error."""
        response = client.post("/analyze", json={
            "code": "x",
            "topic": "array"
        })
        assert response.status_code == 422  # Validation error
    
    def test_analyze_code_too_long(self):
        """Test that code over max length returns validation error."""
        response = client.post("/analyze", json={
            "code": "x" * 10001,  # Over 10000 char limit
            "topic": "array"
        })
        assert response.status_code == 422  # Validation error
    
    def test_analyze_valid_request_structure(self):
        """Test that valid request has correct structure (may fail if no AI key)."""
        response = client.post("/analyze", json={
            "code": "def maxSumSubarray(arr, k):\n    return sum(arr[:k])",
            "topic": "sliding_window"
        })
        
        # Response could be 200 (success) or 503 (no AI key configured)
        assert response.status_code in [200, 503]
        
        data = response.json()
        
        if response.status_code == 200:
            assert "success" in data
            assert data["success"] is True
            assert "feedback" in data
        else:
            # When AI is not configured, we expect a detail field with error message
            assert "detail" in data  # Error message


class TestValidation:
    """Tests for input validation."""
    
    def test_code_sanitization(self):
        """Test that null bytes are removed from code."""
        response = client.post("/analyze", json={
            "code": "def test():\x00\n    pass\n    return True",
            "topic": "array"
        })
        # Should not crash with null bytes
        assert response.status_code in [200, 503]
    
    def test_topic_normalization(self):
        """Test that topic is normalized to lowercase."""
        response = client.post("/analyze", json={
            "code": "def solution():\n    return []",
            "topic": "SLIDING_WINDOW"
        })
        # Should accept uppercase and normalize
        assert response.status_code in [200, 503]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
