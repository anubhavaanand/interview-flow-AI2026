import React, { memo } from 'react';
import { useNavigate } from 'react-router-dom';

// Memoized feature list component
const FeatureList = memo(() => (
  <div style={{ marginBottom: '30px' }}>
    <h3 style={{ marginBottom: '15px' }}>What You'll Get:</h3>
    <ul style={{ listStyle: 'none', textAlign: 'left', maxWidth: '500px', margin: '0 auto' }}>
      {[
        'Real DSA Problems (Similar to interviews)',
        'AI-Powered Code Review & Feedback',
        'Complexity Analysis (Time & Space)',
        '3-Step Improvement Plan'
      ].map((feature, idx) => (
        <li key={idx} style={{ marginBottom: '10px', paddingLeft: '30px', position: 'relative' }}>
          <span style={{ position: 'absolute', left: 0, color: '#007bff', fontWeight: 'bold' }}>✓</span>
          {feature}
        </li>
      ))}
    </ul>
  </div>
));

FeatureList.displayName = 'FeatureList';

function Home() {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate('/interview');
  };

  return (
    <div className="container">
      <div className="header">
        <h1>🎯 interview-flow-AI2026</h1>
        <p>AI-powered DSA Interview Coach</p>
      </div>

      <div className="section" style={{ textAlign: 'center', padding: '40px 20px' }}>
        <h2 style={{ marginBottom: '20px' }}>Welcome to Your DSA Interview Coach</h2>
        
        <p style={{ fontSize: '16px', marginBottom: '20px', color: '#666', maxWidth: '600px', margin: '0 auto 20px' }}>
          Practice coding interview questions with personalized feedback powered by AI.
          Get detailed analysis on time complexity, edge cases, and actionable improvement plans.
        </p>

        <div style={{ marginBottom: '30px' }}>
          <FeatureList />
        </div>

        <button className="button" onClick={handleStart} style={{ padding: '12px 30px', fontSize: '18px' }}>
          Start Mock Interview →
        </button>
      </div>

      <div className="nav-links" style={{ marginTop: '40px' }}>
        <a href="/dashboard">View Dashboard</a>
      </div>
    </div>
  );
}

export default Home;
