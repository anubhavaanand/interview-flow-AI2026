/**
 * API service for communicating with backend
 */

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

/**
 * Fetch a problem from the backend
 */
export const fetchProblem = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/problem`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching problem:', error);
    throw error;
  }
};

/**
 * Submit code for analysis
 */
export const analyzeCode = async (code, topic) => {
  try {
    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        code,
        topic,
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error analyzing code:', error);
    throw error;
  }
};
