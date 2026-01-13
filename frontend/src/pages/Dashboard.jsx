import React, { memo } from 'react';

// Memoized components for better performance
const StatCard = memo(({ title, value }) => (
  <div className="stat-card">
    <h3>{title}</h3>
    <div className="value" style={typeof value === 'string' ? { fontSize: '18px' } : {}}>
      {value}
    </div>
  </div>
));

StatCard.displayName = 'StatCard';

const WeakTopics = memo(({ topics }) => (
  <div style={{ marginBottom: '20px' }}>
    <h3>Topics to Focus On</h3>
    <ul style={{ marginLeft: '20px' }}>
      {topics.map((topic, idx) => (
        <li key={idx} style={{ marginBottom: '8px' }}>{topic}</li>
      ))}
    </ul>
  </div>
));

WeakTopics.displayName = 'WeakTopics';

const SuccessTips = memo(() => (
  <ol style={{ marginLeft: '20px', lineHeight: '1.8' }}>
    <li>Start with easy problems and work your way up</li>
    <li>Focus on understanding the problem before coding</li>
    <li>Think about edge cases and constraints</li>
    <li>Write clean, readable code with meaningful variable names</li>
    <li>Analyze time and space complexity before submitting</li>
    <li>Practice regularly and track your progress</li>
  </ol>
));

SuccessTips.displayName = 'SuccessTips';

function Dashboard() {
  // Hardcoded stats for MVP
  const stats = {
    problemsSolved: 0,
    weakTopics: ['Sliding Window', 'Dynamic Programming'],
    readinessScore: 'Beginner',
    totalAttempts: 0
  };

  return (
    <div className="container">
      <div className="header">
        <h1>🎯 interview-flow-AI2026</h1>
        <p>Your Progress Dashboard</p>
      </div>

      <div className="stats-grid">
        <StatCard title="Problems Solved" value={stats.problemsSolved} />
        <StatCard title="Total Attempts" value={stats.totalAttempts} />
        <StatCard title="Readiness Level" value={stats.readinessScore} />
      </div>

      <div className="section">
        <h2>📈 Your Performance</h2>
        <p style={{ marginBottom: '15px' }}>Keep practicing to improve your interview readiness!</p>
        
        <WeakTopics topics={stats.weakTopics} />
      </div>

      <div className="section">
        <h2>💡 Tips for Success</h2>
        <SuccessTips />
      </div>

      <div className="nav-links">
        <a href="/">← Back to Home</a>
        <a href="/interview">Start Practicing</a>
      </div>
    </div>
  );
}

export default Dashboard;
