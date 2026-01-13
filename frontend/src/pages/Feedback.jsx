import React, { useState, useEffect, memo } from 'react';

// Memoized components for better performance
const FeedbackSection = memo(({ title, children, emoji }) => (
  <div className="feedback-section">
    <h3>{emoji} {title}</h3>
    {children}
  </div>
));

FeedbackSection.displayName = 'FeedbackSection';

const ImprovementPlan = memo(({ steps }) => (
  <ol className="improvement-steps">
    {steps && steps.map((step, idx) => (
      <li key={idx}>{step}</li>
    ))}
  </ol>
));

ImprovementPlan.displayName = 'ImprovementPlan';

const LoadingSkeleton = memo(() => (
  <div className="container">
    <div className="header">
      <h1>🎯 interview-flow-AI2026</h1>
      <p>Loading Feedback...</p>
    </div>
    <div className="loading-skeleton">
      <div className="skeleton-box" style={{ height: '150px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '200px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '150px' }}></div>
    </div>
  </div>
));

LoadingSkeleton.displayName = 'LoadingSkeleton';

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
    return <LoadingSkeleton />;
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
            <FeedbackSection title="Time Complexity" emoji="⏱️">
              <p>{feedback.time_complexity}</p>
            </FeedbackSection>

            <FeedbackSection title="Space Complexity" emoji="💾">
              <p>{feedback.space_complexity}</p>
            </FeedbackSection>

            <FeedbackSection title="Edge Cases" emoji="⚠️">
              <p>{feedback.edge_cases}</p>
            </FeedbackSection>

            <FeedbackSection title="Code Quality" emoji="✨">
              <p>{feedback.code_quality}</p>
            </FeedbackSection>

            <FeedbackSection title="3-Step Improvement Plan" emoji="🚀">
              <ImprovementPlan steps={feedback.improvement_plan} />
            </FeedbackSection>
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
