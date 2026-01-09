import React from 'react';

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
        <div className="stat-card">
          <h3>Problems Solved</h3>
          <div className="value">{stats.problemsSolved}</div>
        </div>
        <div className="stat-card">
          <h3>Total Attempts</h3>
          <div className="value">{stats.totalAttempts}</div>
        </div>
        <div className="stat-card">
          <h3>Readiness Level</h3>
          <div className="value" style={{ fontSize: '18px' }}>{stats.readinessScore}</div>
        </div>
      </div>

      <div className="section">
        <h2>📈 Your Performance</h2>
        <p style={{ marginBottom: '15px' }}>Keep practicing to improve your interview readiness!</p>
        
        <div style={{ marginBottom: '20px' }}>
          <h3>Topics to Focus On</h3>
          <ul style={{ marginLeft: '20px' }}>
            {stats.weakTopics.map((topic, idx) => (
              <li key={idx} style={{ marginBottom: '8px' }}>{topic}</li>
            ))}
          </ul>
        </div>
      </div>

      <div className="section">
        <h2>💡 Tips for Success</h2>
        <ol style={{ marginLeft: '20px', lineHeight: '1.8' }}>
          <li>Start with easy problems and work your way up</li>
          <li>Focus on understanding the problem before coding</li>
          <li>Think about edge cases and constraints</li>
          <li>Write clean, readable code with meaningful variable names</li>
          <li>Analyze time and space complexity before submitting</li>
          <li>Practice regularly and track your progress</li>
        </ol>
      </div>

      <div className="nav-links">
        <a href="/">← Back to Home</a>
        <a href="/interview">Start Practicing</a>
      </div>
    </div>
  );
}

export default Dashboard;
