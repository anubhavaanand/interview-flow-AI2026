import React, { useState, useEffect, memo } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchProblem, analyzeCode } from '../api';

// Memoized components to prevent unnecessary re-renders
const ProblemDisplay = memo(({ problem }) => (
  <>
    <div className="feedback-section">
      <h3>Problem Description</h3>
      <p>{problem.description}</p>
    </div>

    <div className="feedback-section">
      <h3>Constraints</h3>
      <p style={{ fontSize: '14px', color: '#666' }}>{problem.constraints}</p>
    </div>

    <div className="feedback-section">
      <h3>Example</h3>
      <pre style={{
        backgroundColor: '#f8f9fa',
        padding: '12px',
        borderRadius: '4px',
        fontSize: '14px',
        overflow: 'auto'
      }}>
        {problem.example}
      </pre>
    </div>
  </>
));

ProblemDisplay.displayName = 'ProblemDisplay';

const LoadingSkeleton = memo(() => (
  <div className="container">
    <div className="header">
      <h1>🎯 interview-flow-AI2026</h1>
      <p>Mock Interview</p>
    </div>
    <div className="loading-skeleton">
      <div className="skeleton-box" style={{ height: '60px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '120px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '300px' }}></div>
    </div>
  </div>
));

LoadingSkeleton.displayName = 'LoadingSkeleton';

function Interview() {
  const navigate = useNavigate();
  const [problem, setProblem] = useState(null);
  const [code, setCode] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);

  // Load problem on mount
  useEffect(() => {
    const loadProblem = async () => {
      try {
        const data = await fetchProblem();
        setProblem(data);
        // Pre-fill with function signature
        setCode(data.function_signature || '');
      } catch (err) {
        setError('Failed to load problem. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    loadProblem();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!code.trim()) {
      setError('Please write some code before submitting.');
      return;
    }

    setSubmitting(true);
    setError(null);

    try {
      const result = await analyzeCode(code, problem.topic);

      if (result.success) {
        // Store feedback in session storage for the Feedback page
        sessionStorage.setItem('feedback', JSON.stringify({
          feedback: result.feedback,
          problem: problem,
          code: code,
        }));
        navigate('/feedback');
      } else {
        setError(result.error || 'Failed to analyze code. Please try again.');
      }
    } catch (err) {
      setError('Error submitting code. Please check your connection and try again.');
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <LoadingSkeleton />;
  }

  return (
    <div className="container">
      <div className="header">
        <h1>🎯 interview-flow-AI2026</h1>
        <p>Mock Interview - {problem?.topic || 'DSA Problem'}</p>
      </div>

      {error && <div className="error">{error}</div>}

      {problem && (
        <div className="section">
          <h2>{problem.title}</h2>
          <ProblemDisplay problem={problem} />
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="section">
          <h2>Your Solution</h2>
          <textarea
            className="code-editor"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            placeholder="Write your Python code here..."
          />
        </div>

        <div className="section" style={{ textAlign: 'center' }}>
          <button
            type="submit"
            className="button"
            disabled={submitting}
            style={{ padding: '12px 30px', fontSize: '16px' }}
          >
            {submitting ? 'Analyzing...' : 'Submit for Analysis →'}
          </button>
        </div>
      </form>

      <div className="nav-links">
        <a href="/">← Back to Home</a>
        <a href="/dashboard">View Dashboard</a>
      </div>
    </div>
  );
}

export default Interview;
