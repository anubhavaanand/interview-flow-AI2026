/**
 * API service for communicating with backend
 * Includes timeout handling, retry logic, and error interceptors
 */

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
const REQUEST_TIMEOUT = 30000; // 30 seconds
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000; // 1 second initial delay

/**
 * Sleep utility for retry delays
 */
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

/**
 * Fetch with timeout support
 */
const fetchWithTimeout = async (url, options = {}, timeout = REQUEST_TIMEOUT) => {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  
  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(id);
    return response;
  } catch (error) {
    clearTimeout(id);
    if (error.name === 'AbortError') {
      throw new Error('Request timeout - please try again');
    }
    throw error;
  }
};

/**
 * Retry logic with exponential backoff
 */
const fetchWithRetry = async (url, options = {}, retries = MAX_RETRIES) => {
  let lastError;
  
  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetchWithTimeout(url, options);
      
      // Only retry on server errors (5xx) or network errors
      if (response.ok || response.status < 500) {
        return response;
      }
      
      lastError = new Error(`Server error: ${response.status}`);
    } catch (error) {
      lastError = error;
      
      // Don't retry on client errors (4xx)
      if (error.message.includes('4')) {
        throw error;
      }
    }
    
    // Wait before retrying (exponential backoff)
    if (i < retries - 1) {
      const delay = RETRY_DELAY * Math.pow(2, i);
      await sleep(delay);
    }
  }
  
  throw new Error(`Request failed after ${retries} attempts: ${lastError.message}`);
};

/**
 * Global error handler for API responses
 */
const handleResponse = async (response) => {
  if (!response.ok) {
    let errorMessage = `HTTP error! status: ${response.status}`;
    
    try {
      const errorData = await response.json();
      errorMessage = errorData.detail || errorData.error || errorMessage;
    } catch (e) {
      // Could not parse error response
    }
    
    throw new Error(errorMessage);
  }
  
  return await response.json();
};

/**
 * Fetch a problem from the backend
 */
export const fetchProblem = async () => {
  try {
    const response = await fetchWithRetry(`${API_BASE_URL}/problem`);
    return await handleResponse(response);
  } catch (error) {
    console.error('Error fetching problem:', error);
    throw new Error(
      error.message || 'Failed to load problem. Please check your connection and try again.'
    );
  }
};

/**
 * Submit code for analysis
 */
export const analyzeCode = async (code, topic) => {
  try {
    const response = await fetchWithRetry(
      `${API_BASE_URL}/analyze`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code,
          topic,
        }),
      }
    );

    return await handleResponse(response);
  } catch (error) {
    console.error('Error analyzing code:', error);
    throw new Error(
      error.message || 'Failed to analyze code. Please check your connection and try again.'
    );
  }
};
