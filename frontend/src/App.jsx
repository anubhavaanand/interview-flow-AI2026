import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

// Lazy load pages for better performance
const Home = lazy(() => import('./pages/Home'));
const Interview = lazy(() => import('./pages/Interview'));
const Feedback = lazy(() => import('./pages/Feedback'));
const Dashboard = lazy(() => import('./pages/Dashboard'));

// Loading component with skeleton screen
const LoadingFallback = () => (
  <div className="container">
    <div className="header">
      <h1>🎯 interview-flow-AI2026</h1>
      <p>Loading...</p>
    </div>
    <div className="loading-skeleton">
      <div className="skeleton-box" style={{ height: '100px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '200px', marginBottom: '20px' }}></div>
      <div className="skeleton-box" style={{ height: '150px' }}></div>
    </div>
  </div>
);

function App() {
  return (
    <Router>
      <Suspense fallback={<LoadingFallback />}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/interview" element={<Interview />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;
