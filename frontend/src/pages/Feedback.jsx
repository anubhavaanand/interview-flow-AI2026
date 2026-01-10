import React, { useState, useEffect } from 'react';

function Feedback() {
  const [feedbackData, setFeedbackData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Retrieve feedback from session storage
    const stored = sessionStorage.getItem('feedback');
    if (stored) {
      try {
        const data = JSON.parse(stored);
        setFeedbackData(data);
      } catch (err) {
        console.error('Failed to parse feedback:', err);
      }
    }
    setLoading(false);
  }, []);

  if (loading) {
    return (
      <div className="container">
        <div className="header">
          <h1>🎯 interview-flow-AI2026</h1>
          <p>Loading Feedback...</p>
        </div>
        <div className="loading">Loading your feedback...</div>
      </div>
    );
  }

  if (!feedbackData) {
    return (
      <div className="container">
        <div className="header">
          <h1>🎯 interview-flow-AI2026</h1>
          <p>Feedback</p>
        </div>
        <div className="section error">
          <p>No feedback available. Please submit code from the Interview page.</p>
        </div>
        <div className="nav-links">
          <a href="/interview">← Back to Interview</a>
        </div>
      </div>
    );
  }

  const { feedback, problem, code } = feedbackData;

  return (
    <div className="container">
      <div className="header">
        <h1>🎯 interview-flow-AI2026</h1>
        <p>AI Code Review & Feedback</p>
      </div>

      <div className="section">
        <h2>{problem.title}</h2>
        <div className="feedback-section">
          <h3>Your Submission</h3>
          <pre style={{
            backgroundColor: '#f8f9fa',
            padding: '12px',
            borderRadius: '4px',
            fontSize: '13px',
            overflow: 'auto',
            maxHeight: '300px'
          }}>
            {code}
          </pre>
        </div>
      </div>

      <div className="section">
        <h2>📊 AI Feedback Analysis</h2>

        {feedback && (
          <div className="feedback-content">
            <div className="feedback-section">
              <h3>⏱️ Time Complexity</h3>
              <p>{feedback.time_complexity}</p>
            </div>

            <div className="feedback-section">
              <h3>💾 Space Complexity</h3>
              <p>{feedback.space_complexity}</p>
            </div>

            <div className="feedback-section">
              <h3>⚠️ Edge Cases</h3>
              <p>{feedback.edge_cases}</p>
            </div>

            <div className="feedback-section">
              <h3>✨ Code Quality</h3>
              <p>{feedback.code_quality}</p>
            </div>

            <div className="feedback-section">
              <h3>🚀 3-Step Improvement Plan</h3>
              <ol className="improvement-steps">
                {feedback.improvement_plan && feedback.improvement_plan.map((step, idx) => (
                  <li key={idx}>{step}</li>
                ))}
              </ol>
            </div>
          </div>
        )}
      </div>

      <div className="nav-links">
        <a href="/interview">← Try Another Problem</a>
        <a href="/">Back to Home</a>
        <a href="/dashboard">View Dashboard</a>
      </div>
    </div>
  );
}

export default Feedback;
