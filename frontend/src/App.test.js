/**
 * Basic component tests for the React frontend
 * Run with: npm test
 */

import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';

// Helper to render components with router
const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('Home Component', () => {
  test('renders home page title', () => {
    renderWithRouter(<Home />);
    const titleElement = screen.getByText(/interview-flow-AI2026/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders start button', () => {
    renderWithRouter(<Home />);
    const buttonElement = screen.getByText(/Start Mock Interview/i);
    expect(buttonElement).toBeInTheDocument();
  });

  test('renders feature list', () => {
    renderWithRouter(<Home />);
    expect(screen.getByText(/Real DSA Problems/i)).toBeInTheDocument();
    expect(screen.getByText(/AI-Powered Code Review/i)).toBeInTheDocument();
  });
});

describe('Dashboard Component', () => {
  test('renders dashboard title', () => {
    renderWithRouter(<Dashboard />);
    const titleElement = screen.getByText(/Your Progress Dashboard/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders stat cards', () => {
    renderWithRouter(<Dashboard />);
    expect(screen.getByText(/Problems Solved/i)).toBeInTheDocument();
    expect(screen.getByText(/Total Attempts/i)).toBeInTheDocument();
    expect(screen.getByText(/Readiness Level/i)).toBeInTheDocument();
  });

  test('renders tips section', () => {
    renderWithRouter(<Dashboard />);
    expect(screen.getByText(/Tips for Success/i)).toBeInTheDocument();
  });
});
