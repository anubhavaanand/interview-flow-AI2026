# 🛠️ What's Running, What I'm Setting Up, and How

## Executive Summary

**What's Running Now:**
1. **Backend (FastAPI)** - Python server on `localhost:8000` that serves DSA problems and analyzes code
2. **Frontend (React)** - JavaScript server on `localhost:3000` that provides the user interface
3. **VS Code Language Servers** - TypeScript, Python, ESLint, etc. for code editor features

**What I've Set Up:**
1. **Startup Script (`start.sh`)** - Intelligent script that starts/stops both services with port conflict detection
2. **Environment Setup (`setup-env.sh`)** - Interactive script to configure Azure OpenAI credentials
3. **This Document** - Clear explanation of the architecture and how pieces fit together

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                       User Browser (Port 3000)                  │
│                      React Frontend (SPA)                       │
├─────────────────────────────────────────────────────────────────┤
│  Pages: Home → Interview → Feedback → Dashboard                │
│  Language: JavaScript/JSX with React Hooks                      │
│  Build: npm start (Create React App development server)        │
└────────────────────────┬────────────────────────────────────────┘
                         │ API Calls (JSON)
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Backend (Port 8000)                          │
│                    FastAPI (Python)                             │
├─────────────────────────────────────────────────────────────────┤
│  Routes:                                                        │
│  - GET /problem          → Returns DSA problem JSON             │
│  - POST /analyze         → Sends code to Azure OpenAI           │
│  - GET /                 → Health check                         │
│                                                                 │
│  Dependencies:                                                  │
│  - fastapi               (web framework)                        │
│  - uvicorn              (ASGI server)                           │
│  - openai               (Azure SDK)                             │
│  - python-dotenv        (load .env file)                        │
└────────────────────────┬────────────────────────────────────────┘
                         │ API Call (HTTPS)
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│                   Azure OpenAI (Cloud)                          │
│           GPT-4-turbo Model (Code Analysis)                     │
├─────────────────────────────────────────────────────────────────┤
│  Input: User's Python code + Prompt template                    │
│  Output: Structured feedback (complexity, edge cases, etc.)     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 What Each Component Does

### Frontend (React) - Port 3000
**Purpose:** User interface for the interview coaching experience

**Files:**
- `frontend/src/App.jsx` - Routes the 4 pages
- `frontend/src/api.js` - Service layer that calls backend
- `frontend/src/pages/Home.jsx` - Landing page
- `frontend/src/pages/Interview.jsx` - Problem display + code editor
- `frontend/src/pages/Feedback.jsx` - AI feedback display
- `frontend/src/pages/Dashboard.jsx` - Stats display

**Flow:**
```
User clicks "Start Interview"
    ↓
React Router navigates to /interview
    ↓
Interview.jsx calls api.fetchProblem()
    ↓
Backend returns problem JSON
    ↓
User writes code in textarea
    ↓
User clicks "Submit"
    ↓
Interview.jsx calls api.analyzCode(code, topic)
    ↓
Backend calls Azure OpenAI
    ↓
Feedback appears on /feedback page
```

**Technology:**
- React 18 - Component framework
- React Router v6 - Page navigation
- Fetch API - HTTP requests
- CSS - Styling (minimal but functional)
- Node.js 18+ - Runtime

---

### Backend (FastAPI) - Port 8000
**Purpose:** API server that bridges frontend and Azure OpenAI

**Files:**
- `backend/main.py` - FastAPI application with 3 routes
- `backend/prompts.py` - Prompt templates for Azure OpenAI
- `backend/requirements.txt` - Python dependencies
- `backend/.env` - Secrets (API key, endpoint)
- `backend/venv/` - Python virtual environment

**Key Features:**
1. **CORS Support** - Allows requests from localhost:3000
2. **Lazy Initialization** - Doesn't crash without Azure credentials
3. **Error Handling** - Returns meaningful JSON errors
4. **Hardcoded Problem** - No database needed for MVP

**Routes:**

```python
GET /
├─ Returns: {"status": "ok"}
└─ Purpose: Health check

GET /problem
├─ Returns: DSA problem JSON
├─ Example: Sliding Window Maximum Sum problem
└─ Response format:
    {
        "id": "sliding_window_1",
        "title": "...",
        "description": "...",
        "topic": "sliding_window",
        "function_signature": "def maxSumSubarray(arr, k):\n    pass"
    }

POST /analyze
├─ Body: {"code": "user code here", "topic": "sliding_window"}
├─ Calls: Azure OpenAI API with DSA_FEEDBACK_PROMPT
└─ Returns:
    {
        "success": true,
        "feedback": {
            "time_complexity": "...",
            "space_complexity": "...",
            "edge_cases": "...",
            "code_quality": "...",
            "improvement_plan": [...]
        }
    }
```

**Technology:**
- FastAPI - Web framework (async, fast, auto-docs)
- Uvicorn - ASGI server (runs FastAPI)
- OpenAI Python SDK - Azure OpenAI client
- Pydantic - Data validation
- Python 3.10+ - Runtime

---

## 🚀 How to Use the New Startup Scripts

### Quick Start (Recommended)

```bash
# 1. One-time setup: Configure Azure credentials
./setup-env.sh

# 2. Start everything with one command
./start.sh

# 3. Open browser to http://localhost:3000

# 4. (Optional) View logs
./start.sh logs backend
./start.sh logs frontend
./start.sh logs both
```

### Script Details

#### `start.sh` - Main Startup Script

**What it does:**
1. ✅ Detects if ports are in use and cleans them up
2. ✅ Activates Python virtual environment
3. ✅ Installs dependencies if needed
4. ✅ Loads environment variables from `.env`
5. ✅ Starts backend with `uvicorn`
6. ✅ Starts frontend with `npm start`
7. ✅ Verifies both services are running
8. ✅ Shows status and log locations

**Commands:**
```bash
./start.sh start          # Start both services (default)
./start.sh stop           # Stop both services
./start.sh restart        # Restart both services
./start.sh status         # Show service status
./start.sh logs           # Show both logs (live)
./start.sh logs backend   # Show backend logs only
./start.sh logs frontend  # Show frontend logs only
```

**Why this solves MCP issues:**
- Automatically kills processes on ports before starting (no conflicts)
- Runs services in background (no terminal blocking)
- Logs to `/tmp/backend.log` and `/tmp/frontend.log`
- Health checks verify services started correctly
- No manual restarts needed

---

#### `setup-env.sh` - Environment Configuration

**What it does:**
1. Interactive prompts for Azure credentials
2. Creates `backend/.env` with encrypted variables
3. Validates endpoint format
4. Sets deployment name (defaults to `gpt-4`)

**Usage:**
```bash
./setup-env.sh
# Follow prompts, paste:
# - API Key from Azure Portal
# - Endpoint URL (e.g., https://your-resource.openai.azure.com/)
# - Deployment name (optional, defaults to gpt-4)
```

**Example Output:**
```
Azure OpenAI API Key: sk-abc123...xyz789
Azure OpenAI Endpoint: https://myresource.openai.azure.com/
Azure OpenAI Deployment Name [gpt-4]: gpt-4-turbo
✅ Environment setup complete!
Configuration saved to: backend/.env
```

---

## 📊 What Was Previously Running and Why Issues Occurred

### Old Manual Process (Causing Restarts)
```bash
# Terminal 1: Backend (blocks terminal)
cd backend
source venv/bin/activate
uvicorn main:app --reload

# Terminal 2: Frontend (blocks terminal)
cd frontend
npm start

# Problem: If either process dies, need to manually restart in terminal
# Problem: If port already in use, both processes fail with cryptic errors
# Problem: Hard to see logs from both services simultaneously
```

### What "MCP Server Error" Likely Was
The "MCP server restart" was likely one of:
1. **Port Conflict** - Port 8000 or 3000 already in use
2. **Dependencies Missing** - npm or pip packages not installed
3. **Environment Variables** - Azure credentials not set, causing main.py to hang
4. **Process Zombie** - Previous process not fully killed, blocking restart
5. **VS Code Language Server Crash** - Terminal getting restarted by VS Code extension

### How New Scripts Fix This
```bash
# Single command:
./start.sh

# What happens:
1. Checks ports 8000 and 3000
2. Kills any existing processes using those ports (lsof + kill -9)
3. Waits 2 seconds for cleanup
4. Starts backend in background → /tmp/backend.log
5. Waits 3 seconds for startup
6. Tests with curl if backend is responding
7. Starts frontend in background → /tmp/frontend.log
8. Waits 8 seconds for startup
9. Tests with curl if frontend is responding
10. Shows clean status summary

# Result: No manual restarts, no conflicts, clear logs
```

---

## 🔍 Monitoring and Troubleshooting

### Check Service Status Anytime
```bash
./start.sh status
# Output:
# ✅ Backend: http://localhost:8000
# ✅ Frontend: http://localhost:3000
```

### View Live Logs
```bash
# Both services
./start.sh logs both

# Just backend
./start.sh logs backend

# Just frontend (shows build output)
./start.sh logs frontend
```

### Stop All Services Cleanly
```bash
./start.sh stop
# Output:
# ⚠️  Port 8000 (Backend) is in use. Cleaning up...
# ✅ Cleaned up port 8000
# ⚠️  Port 3000 (Frontend) is in use. Cleaning up...
# ✅ Cleaned up port 3000
```

### Restart Everything
```bash
./start.sh restart
# Stops both, waits 2 seconds, starts both
```

---

## 📝 Process Flow - Complete Example

### User Journey (What's Happening Behind Scenes)

```
1. USER OPENS BROWSER
   http://localhost:3000
   ↓
   React App Loads (frontend/src/App.jsx)

2. USER SEES HOME PAGE
   "Start Mock Interview" button
   ↓
   React Router setup complete

3. USER CLICKS "START MOCK INTERVIEW"
   Frontend calls: api.fetchProblem()
   ↓
   fetch("http://localhost:8000/problem", {...})

4. BACKEND RECEIVES GET /problem
   main.py route:
   - Returns hardcoded problem JSON
   - 200 OK response
   ↓
   Frontend receives problem data

5. INTERVIEW PAGE RENDERS
   - Problem title and description
   - Code textarea with function signature
   - Submit button
   ↓
   User writes Python code

6. USER SUBMITS CODE
   Frontend calls: api.analyzCode(code, "sliding_window")
   ↓
   POST to http://localhost:8000/analyze
   Body: {"code": "user code...", "topic": "sliding_window"}

7. BACKEND RECEIVES POST /analyze
   main.py route:
   - Loads prompt template from prompts.py
   - Initializes Azure OpenAI client
   - Makes API call to Azure with:
     * User's code
     * DSA_FEEDBACK_PROMPT template
   ↓
   Azure OpenAI processes request (3-10 seconds)

8. AZURE OPENAI GENERATES FEEDBACK
   GPT-4-turbo analyzes code and returns:
   - Time complexity assessment
   - Space complexity assessment
   - Edge case issues
   - Code quality suggestions
   - 3-step improvement plan

9. BACKEND RETURNS FEEDBACK
   200 OK response with feedback JSON
   ↓
   Frontend receives structured feedback

10. FEEDBACK PAGE DISPLAYS RESULTS
    - Renders complexity analysis
    - Shows edge case issues
    - Displays improvement plan
    ↓
    User sees comprehensive feedback

11. USER NAVIGATES TO DASHBOARD
    - Shows stats (hardcoded for MVP)
    - Weak topics
    - Readiness score
```

---

## 🎯 Current Status

**✅ What's Working:**
- Both services can start and run simultaneously
- API communication between frontend and backend
- Hardcoded problem is delivered correctly
- No critical code errors
- Git repository synchronized

**⏳ What Needs Azure Credentials:**
- `POST /analyze` returns error without AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT
- Full end-to-end flow (submit code → get feedback) blocked
- This is expected - credentials are secrets, never committed to git

**🚀 Next Steps (In Order):**
1. Run `./setup-env.sh` to configure Azure credentials
2. Run `./start.sh` to start both services
3. Test flow: Home → Interview → Submit code → See feedback
4. Create pitch deck (Phase 5)
5. Record demo videos (Phase 5)
6. Submit to Imagine Cup (Phase 6)

---

## 🔐 Security Note

**Never commit `.env` to Git!**

The file is already in `.gitignore`, but verify:
```bash
# Check that .env is ignored
cat .gitignore | grep ".env"
# Output: .env

# Verify it's not in git
git status
# Should NOT show backend/.env as tracked
```

---

## 📞 Quick Reference

| Task | Command |
|------|---------|
| Start services | `./start.sh` |
| Configure Azure | `./setup-env.sh` |
| Stop services | `./start.sh stop` |
| Restart services | `./start.sh restart` |
| Check status | `./start.sh status` |
| View logs | `./start.sh logs both` |
| Backend logs only | `./start.sh logs backend` |
| Frontend logs only | `./start.sh logs frontend` |
| Kill port 8000 | `lsof -i :8000 \| awk 'NR!=1 {print $2}' \| xargs kill -9` |
| Kill port 3000 | `lsof -i :3000 \| awk 'NR!=1 {print $2}' \| xargs kill -9` |

---

**Questions?** Check the error logs:
- Backend: `tail -f /tmp/backend.log`
- Frontend: `tail -f /tmp/frontend.log`
