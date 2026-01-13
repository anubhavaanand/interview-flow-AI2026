# interview-flow-AI2026

AI-powered DSA interview coach for coding interview preparation.

## 🎯 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- GitHub personal access token (for GitHub Models API)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables
export GITHUB_TOKEN="your-github-token"  # Get from https://github.com/settings/tokens

# Start server (port 8000)
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
BROWSER=none npm start  # Starts on port 3000
```

## 🌐 Architecture

```
┌─────────────────────────────────────────┐
│  Frontend (React)                       │
│  http://localhost:3000                  │
│  - Home, Interview, Feedback, Dashboard │
└─────────────────┬───────────────────────┘
                  │ HTTP REST API
┌─────────────────v───────────────────────┐
│  Backend (FastAPI)                      │
│  http://localhost:8000                  │
│  - GET /problem                         │
│  - POST /analyze                        │
└─────────────────┬───────────────────────┘
                  │ Azure OpenAI API
┌─────────────────v───────────────────────┐
│  Azure OpenAI (GPT-4-turbo)             │
│  Code feedback & analysis               │
└─────────────────────────────────────────┘
```

## 📂 Project Structure

```
interview-flow-AI2026/
├── backend/                    # FastAPI backend
│   ├── main.py                # Main application
│   ├── prompts.py             # Azure OpenAI prompts
│   ├── requirements.txt        # Python dependencies
│   └── venv/                  # Virtual environment
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── pages/             # React pages
│   │   ├── App.jsx            # Router setup
│   │   ├── api.js             # API service
│   │   └── App.css            # Styles
│   └── package.json
├── docs/                       # Documentation
│   ├── mvp-scope.md           # MVP requirements
│   └── tech-stack.md          # Technical stack
└── .github/
    └── copilot-instructions.md # AI agent guide
```

## 🚀 Features (MVP)

### Home Page
- Landing page with project overview
- "Start Mock Interview" button
- Navigation to dashboard

### Interview Page
- Displays DSA problem (Sliding Window)
- Code editor for writing solutions
- Submit button to analyze code

### Feedback Page
- AI-generated feedback on:
  - Time Complexity
  - Space Complexity
  - Edge Cases
  - Code Quality
  - 3-Step Improvement Plan

### Dashboard Page
- Problems solved count
- Weak topics identification
- Readiness score
- Tips for success

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/problem` | Get DSA problem |
| POST | `/analyze` | Analyze code + get feedback |

### Example Requests

**Get Problem:**
```bash
curl http://localhost:8000/problem
```

**Analyze Code:**
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def solution(arr, k):\n    return max(sum(arr[i:i+k]) for i in range(len(arr)-k+1))",
    "topic": "sliding_window"
  }'
```

## 📝 Environment Variables

Create `.env` file in `backend/` directory:

```
AZURE_OPENAI_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

Template available in `.env.example`

## 🧪 Testing

### Backend
```bash
cd backend

# Run validation script
python validate_startup.py

# Run unit tests
pytest tests/ -v

# Run integration tests
pytest tests/test_integration.py -v

# Test individual endpoints
curl http://localhost:8000/problem | jq
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"code":"def f():\n  pass","topic":"sliding_window"}'
```

### Frontend
```bash
cd frontend

# Run component tests
npm test

# Run ESLint
npm run lint  # (if configured in package.json)

# Build production bundle
npm run build
```

## ⚡ Performance Optimizations

### Frontend
- **Lazy Loading**: Pages load on-demand, reducing initial bundle size by ~30-40%
- **React.memo()**: Prevents unnecessary re-renders of components
- **Debounce Hook**: Custom useDebounce hook available for future optimization features
- **Skeleton Screens**: Better perceived performance with loading placeholders

### Backend
- **Response Caching**: Problem endpoint uses LRU cache for faster responses
- **Rate Limiting**: 30 req/min for problems, 10 req/min for analysis
- **Request Validation**: Pydantic validators ensure data quality
- **Comprehensive Logging**: All requests logged to `api.log` for debugging

### API Integration
- **Timeout Handling**: 30-second timeout prevents hanging requests
- **Retry Logic**: Exponential backoff for failed requests (max 3 retries)
- **Error Interceptors**: Global error handling with user-friendly messages

## 🔒 Security Features

- **Input Sanitization**: Code submissions sanitized for null bytes and validated
- **Rate Limiting**: Prevents abuse with slowapi middleware
- **Environment Validation**: Startup checks ensure proper configuration
- **HTTPS Ready**: Production mode with HTTPS enforcement notes

## 🛠️ Developer Tools

- **ESLint**: Frontend code quality checks (`.eslintrc.json`)
- **Pre-commit Hooks**: Automatic formatting and validation (`.pre-commit-config.yaml`)
- **Validation Script**: `backend/validate_startup.py` checks environment
- **Comprehensive Tests**: Unit and integration tests for backend and frontend

## 📚 Documentation

### Submission Materials
- **[READY_TO_SUBMIT.md](READY_TO_SUBMIT.md)** ⭐ START HERE - Final submission checklist & status
- **[PITCH_DECK.md](PITCH_DECK.md)** - 15 slides + speaking notes (1/3/5-min variants)
- **[DEMO_VIDEOS.md](DEMO_VIDEOS.md)** - Complete video scripts + production guide
- **[RECORD_TODAY.md](RECORD_TODAY.md)** - Quick reference for recording videos
- **[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Step-by-step form completion guide

### Technical Documentation
- **[Copilot Instructions](.github/copilot-instructions.md)** - AI agent development guide
- **[Frontend README](frontend/README.md)** - React app architecture
- **[Backend README](backend/README.md)** - FastAPI setup (if exists)
- **[MVP Scope](docs/mvp-scope.md)** - Feature requirements

## 🚀 Imagine Cup 2026 Submission

### Status
- ✅ MVP Complete (Frontend + Backend + AI Integration)
- ✅ Both services running (http://localhost:3000 and 8000)
- ✅ GitHub Models API integrated (gpt-4o)
- ⏳ Videos pending (record today)
- ⏳ Form submission (tomorrow at 1:00 PM IST)

### Deadline
**January 10, 2026, 1:29 PM IST** (~17 hours remaining)

### Next Steps
1. **Today:** Record demo + pitch videos (use [RECORD_TODAY.md](RECORD_TODAY.md))
2. **Tomorrow AM:** Fill Imagine Cup form (use [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md))
3. **Tomorrow 1:00 PM:** Submit before deadline

### Quick Links
- **GitHub Repository**: https://github.com/anubhavaanand/interview-flow-AI2026
- **Demo**: Run `./start.sh` to test locally
- **Pitch**: See [PITCH_DECK.md](PITCH_DECK.md) for 3-minute variant

## 🤝 Contributing

This is an MVP for Imagine Cup 2026. All development follows the [Copilot Instructions](.github/copilot-instructions.md).

## 📄 License

This project is part of the Imagine Cup 2026 submission.

## 🔧 Troubleshooting Guide

### Backend Issues

#### Problem: "GitHub token not configured" error
**Solution:**
1. Create a GitHub personal access token at https://github.com/settings/tokens
2. Set the environment variable: `export GITHUB_TOKEN="your_token"`
3. Or run the setup script: `./setup-env.sh`

#### Problem: Backend fails to start
**Solution:**
1. Run validation script: `cd backend && python validate_startup.py`
2. Install missing dependencies: `pip install -r requirements.txt`
3. Check Python version (3.10+ required): `python --version`

#### Problem: Rate limit errors
**Solution:**
- Wait 1 minute before retrying (rate limits: 30/min for problems, 10/min for analysis)
- Check logs in `backend/api.log` for detailed error messages

#### Problem: Import errors or module not found
**Solution:**
1. Activate virtual environment: `source venv/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check you're in the correct directory: `cd backend`

### Frontend Issues

#### Problem: "Failed to load problem" error
**Solution:**
1. Verify backend is running on port 8000: `curl http://localhost:8000/`
2. Check CORS settings in backend/main.py
3. Verify API URL in frontend/.env or frontend/src/api.js

#### Problem: Frontend build fails
**Solution:**
1. Clear node modules: `rm -rf node_modules package-lock.json`
2. Reinstall dependencies: `npm install`
3. Check Node version (16+ required): `node --version`

#### Problem: "Request timeout" errors
**Solution:**
- The backend may be processing a complex analysis
- Wait 30 seconds and try again
- Check backend logs for detailed errors
- Ensure stable internet connection for AI API calls

#### Problem: Blank screen or routing issues
**Solution:**
1. Clear browser cache and cookies
2. Check browser console for errors (F12)
3. Verify all routes in App.jsx are correctly configured
4. Try accessing directly: http://localhost:3000/

### Performance Issues

#### Problem: Slow page loads
**Solution:**
- Hard refresh browser: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
- Check network tab in browser DevTools for slow requests
- Verify backend response times in logs

#### Problem: High memory usage
**Solution:**
- Restart both frontend and backend services
- Clear browser cache
- Check for memory leaks in browser DevTools

### Testing Issues

#### Problem: Backend tests fail
**Solution:**
```bash
cd backend
pytest tests/ -v
# If tests fail due to missing AI credentials, that's expected
# Tests are designed to handle both configured and unconfigured states
```

#### Problem: Frontend tests fail
**Solution:**
```bash
cd frontend
npm test
# Press 'a' to run all tests
# Some tests may require specific browser configurations
```

### Environment Setup Issues

#### Problem: .env file not working
**Solution:**
1. Copy example file: `cp backend/.env.example backend/.env`
2. Edit with your credentials: `nano backend/.env`
3. Ensure no extra spaces or quotes around values
4. Restart the backend server

#### Problem: Pre-commit hooks failing
**Solution:**
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Network and CORS Issues

#### Problem: CORS errors in browser console
**Solution:**
1. Verify backend allows frontend origin in main.py
2. Check that both services are running on expected ports
3. Try using 127.0.0.1 instead of localhost (or vice versa)

### Logs and Debugging

**Backend logs location:** `backend/api.log`
**Frontend console:** Press F12 in browser

**Enable debug mode:**
```bash
# Backend: Check logs in api.log
tail -f backend/api.log

# Frontend: Check browser console (F12)
```

### Getting Help

If you're still experiencing issues:
1. Check the logs in `backend/api.log`
2. Review browser console for frontend errors
3. Ensure all prerequisites are installed (Python 3.10+, Node 16+)
4. Verify environment variables are set correctly
5. Try the validation script: `python backend/validate_startup.py`

---

**Status**: 🟢 READY FOR SUBMISSION  
**Last Updated**: January 13, 2026  
**Deadline**: January 10, 2026, 1:29 PM IST
