# 🏗️ Complete System Architecture Diagram

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INTERACTION LAYER                          │
│                                                                         │
│                   Web Browser (Chrome/Firefox/Safari)                   │
│                   http://localhost:3000                                 │
│                                                                         │
│  ┌────────────────┬────────────────┬────────────────┬────────────────┐ │
│  │     HOME       │   INTERVIEW    │   FEEDBACK     │   DASHBOARD    │ │
│  │   Page (/)     │   Page (/i...)  │   Page (/f...) │   Page (/d...) │ │
│  └────────────────┴────────────────┴────────────────┴────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
                          ↕ (JSON API Calls)
┌──────────────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER (Localhost)                       │
│                                                                          │
│  FRONTEND (React.js)                  BACKEND (FastAPI)                 │
│  Port: 3000                          Port: 8000                         │
│  ┌──────────────────────┐            ┌──────────────────────┐           │
│  │  React Components    │            │  FastAPI Routes      │           │
│  ├──────────────────────┤            ├──────────────────────┤           │
│  │ • Home.jsx          │ GET /problem│ • GET /              │           │
│  │ • Interview.jsx ────├───────────→ ├─ Health check       │           │
│  │ • Feedback.jsx      │ POST /analyze│ • GET /problem       │           │
│  │ • Dashboard.jsx     │────────────→ ├─ Returns problem    │           │
│  │                     │              │ • POST /analyze      │           │
│  ├──────────────────────┤            ├─ Receives code       │           │
│  │ api.js (Services)    │            ├─ Calls Azure OpenAI  │           │
│  ├──────────────────────┤            ├─ Returns feedback    │           │
│  │ • fetchProblem()    │ ←──────────┤ ├──────────────────────┤           │
│  │ • analyzCode()      │ ←──────────┤ │ main.py             │           │
│  │ • fetch wrapper     │            │ │ prompts.py          │           │
│  └──────────────────────┘            │ │ requirements.txt    │           │
│                                      └──────────────────────┘           │
│  Framework: React 18                  Framework: FastAPI                 │
│  Router: React Router v6              Server: Uvicorn (ASGI)            │
│  State: React Hooks                   DB: None (hardcoded MVP)          │
│  Build: Create React App              Language: Python 3.10+            │
└──────────────────────────────────────────────────────────────────────────┘
                        ↕ (HTTPS REST API Call)
┌──────────────────────────────────────────────────────────────────────────┐
│                        CLOUD LAYER (Azure)                              │
│                                                                          │
│  Azure OpenAI Service                                                    │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │  GPT-4-turbo Model                                       │           │
│  ├──────────────────────────────────────────────────────────┤           │
│  │  Input:                                                  │           │
│  │  • User's Python code                                   │           │
│  │  • DSA problem context                                  │           │
│  │  • Structured prompt template                           │           │
│  │                                                          │           │
│  │  Processing:                                            │           │
│  │  • Analyze time complexity                              │           │
│  │  • Analyze space complexity                             │           │
│  │  • Identify edge cases                                  │           │
│  │  • Assess code quality                                  │           │
│  │  • Generate 3-step improvement plan                     │           │
│  │                                                          │           │
│  │  Output:                                                │           │
│  │  • Structured feedback JSON                             │           │
│  │  • Time/Space complexity analysis                       │           │
│  │  • Edge case warnings                                   │           │
│  │  • Actionable improvement steps                         │           │
│  └──────────────────────────────────────────────────────────┘           │
│                                                                          │
│  Authentication:                                                         │
│  • AZURE_OPENAI_KEY (API key)                                           │
│  • AZURE_OPENAI_ENDPOINT (Service URL)                                  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

### User Submits Code (Complete Flow)

```
USER ACTIONS                 FRONTEND (React)           BACKEND (FastAPI)        AZURE OPENAI
─────────────────────────────────────────────────────────────────────────────────────────

1. Load page
│                                                                               
└─ http://localhost:3000
                    │
                    ├─ React Router navigates to /interview
                    │
                    └─ Interview.jsx renders

2. Fetch problem
│
└─ Click interview page
                    │
                    └─ api.fetchProblem() called
                            │
                            └─ GET /problem ──────────────────→ backend/main.py
                                                                │
                                                                └─ Return hardcoded
                                                                   problem JSON
                            ↑────────────────────────────────────┘
                    │
                    ├─ Receive problem JSON
                    │
                    └─ Display in Interview.jsx
                        • Problem title
                        • Description
                        • Function signature
                        • Code textarea

3. Write code
│
└─ User types Python code in textarea
                    │
                    └─ Code stored in React state

4. Submit code
│
└─ Click "Submit"
                    │
                    ├─ api.analyzCode(code, topic) called
                    │
                    └─ POST /analyze ──────────────────────→ backend/main.py
                                                              │
                                                              ├─ Load prompt_template
                                                              │   from prompts.py
                                                              │
                                                              ├─ Initialize Azure
                                                              │   OpenAI client
                                                              │
                                                              ├─ Build request:
                                                              │   • User's code
                                                              │   • Prompt template
                                                              │
                                                              └─ Call Azure API ──→ AZURE CLOUD
                                                                                     │
                                                                                     ├─ Authenticate with
                                                                                     │  AZURE_OPENAI_KEY
                                                                                     │
                                                                                     ├─ Route to GPT-4
                                                                                     │
                                                                                     ├─ Process code
                                                                                     │  analysis
                                                                                     │
                                                                                     └─ Generate feedback
                                                                  ↑───────────────────┘
                                                              (3-10 seconds)
                                                              │
                                                              ├─ Parse response
                                                              │
                                                              ├─ Structure JSON:
                                                              │  {
                                                              │    "time_complexity": "O(n)",
                                                              │    "space_complexity": "O(1)",
                                                              │    "edge_cases": "...",
                                                              │    "code_quality": "...",
                                                              │    "improvement_plan": [...]
                                                              │  }
                                                              │
                                                              └─ Return JSON ─────────────→
                            ↑───────────────────────────────────┘
                    │
                    ├─ Receive feedback JSON
                    │
                    ├─ Store in sessionStorage
                    │
                    └─ Navigate to /feedback
                        (Feedback.jsx)

5. View feedback
│
└─ Feedback page renders
                    │
                    ├─ Read from sessionStorage
                    │
                    ├─ Display:
                    │  • Time complexity
                    │  • Space complexity
                    │  • Edge cases
                    │  • Code quality
                    │  • 3-step improvement plan
                    │
                    └─ User sees AI feedback!

6. Continue
│
└─ Click "Start New Interview" or "Dashboard"
                    │
                    └─ React Router navigates to next page
```

---

## Component Dependency Map

```
React App Structure
═══════════════════

App.jsx
├── Route: "/"
│   └── Home.jsx
│       └── Button → navigate("/interview")
│
├── Route: "/interview"
│   └── Interview.jsx
│       ├── Uses: api.js
│       │   ├── fetchProblem()  → GET /problem
│       │   └── analyzCode()    → POST /analyze
│       │
│       └── State:
│           ├── problemData
│           ├── userCode
│           ├── loading
│           └── error
│
├── Route: "/feedback"
│   └── Feedback.jsx
│       ├── Reads: sessionStorage (from Interview)
│       └── Displays:
│           ├── Complexity analysis
│           ├── Edge cases
│           ├── Improvements
│           └── Navigation buttons
│
└── Route: "/dashboard"
    └── Dashboard.jsx
        └── Displays: (hardcoded stats)
            ├── Problems solved
            ├── Weak topics
            ├── Readiness score
            └── Study tips


FastAPI App Structure
═════════════════════

main.py
├── CORS middleware (allow localhost:3000)
│
├── Route: GET /
│   └── Health check → {"status": "ok"}
│
├── Route: GET /problem
│   └── Return: hardcoded_problem.json
│       {
│           "id": "sliding_window_1",
│           "title": "...",
│           "description": "...",
│           "topic": "sliding_window",
│           "function_signature": "..."
│       }
│
└── Route: POST /analyze
    ├── Input: {"code": "user code", "topic": "sliding_window"}
    │
    ├── Load: prompts.py
    │   └── DSA_FEEDBACK_PROMPT template
    │
    ├── Initialize: Azure OpenAI client
    │   └── Uses env vars:
    │       ├── AZURE_OPENAI_KEY
    │       └── AZURE_OPENAI_ENDPOINT
    │
    ├── Call: Azure API
    │   └── GPT-4-turbo analyzes code
    │
    └── Return: feedback JSON
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

---

## Execution Timeline

### Single Request: "Submit Code"

```
Time    Component       Action                  Duration
────────────────────────────────────────────────────────
0ms     Frontend        User clicks "Submit"    —
1ms     Frontend        api.analyzCode() call   —
5ms     Network         POST to localhost:8000  4ms
10ms    Backend         Receive request         —
11ms    Backend         Load Azure client       2ms
13ms    Backend         Build prompt            1ms
14ms    Backend         Call Azure OpenAI       (async)
        │
14ms    Frontend        Show "Loading..."       —
        │
        │       [Azure Processing]
        │
3000ms  Azure OpenAI    Generate feedback       ~2800ms
        │
3010ms  Backend         Receive response        —
3015ms  Backend         Parse response          5ms
3020ms  Backend         Return to frontend      —
3025ms  Network         Response arrives        5ms
3030ms  Frontend        Receive feedback        —
3035ms  Frontend        Store in sessionStorage —
3040ms  Frontend        Navigate to /feedback   —
3045ms  Feedback.jsx    Display feedback        5ms
        │
        └─ User sees complete AI analysis!

Total time: ~3.05 seconds (mostly Azure processing)
```

---

## Environment Configuration

```
/interview-flow-AI2026/
│
├── backend/
│   ├── main.py                 ← FastAPI application
│   ├── prompts.py              ← Azure OpenAI prompt templates
│   ├── requirements.txt         ← Python dependencies
│   ├── .env                    ← SECRETS (not in git)
│   ├── .env.example            ← Template for .env
│   └── venv/                   ← Python virtual environment
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            ← Router setup
│   │   ├── api.js             ← Backend API service
│   │   ├── App.css            ← Styling
│   │   └── pages/
│   │       ├── Home.jsx
│   │       ├── Interview.jsx
│   │       ├── Feedback.jsx
│   │       └── Dashboard.jsx
│   ├── package.json           ← NPM dependencies
│   └── node_modules/          ← Installed packages
│
├── start.sh                    ← Smart startup script
├── setup-env.sh                ← Azure credential setup
│
├── ENVIRONMENT_SETUP.md        ← Complete documentation
├── QUICK_START_FIX.md          ← Quick reference
├── MCP_FIX_EXPLANATION.md      ← MCP issue + solution
├── README.md                   ← Project overview
│
└── .github/
    └── copilot-instructions.md ← AI agent guide

Configuration Files (.env):
    AZURE_OPENAI_KEY=sk-...
    AZURE_OPENAI_ENDPOINT=https://...
    AZURE_OPENAI_DEPLOYMENT=gpt-4
```

---

## Key Statistics

### Code Size
- **Backend:** ~300 lines (main.py + prompts.py)
- **Frontend:** ~600 lines (4 pages + api + css)
- **Total:** ~900 lines of application code

### Performance Targets
- **Frontend load:** < 2 seconds
- **Problem fetch:** < 500ms
- **Azure feedback:** 2-10 seconds (mostly Azure processing)
- **Total flow:** < 15 seconds

### Resource Usage (Running)
- **Backend Python:** ~40-50 MB RAM
- **Frontend npm server:** ~80-100 MB RAM
- **Combined:** ~150 MB RAM (minimal)

### Dependencies
- **Backend:** 4 main packages (fastapi, uvicorn, openai, python-dotenv)
- **Frontend:** ~200 packages (React ecosystem from create-react-app)
- **Database:** None (MVP - hardcoded data)

---

## Deployment Architecture (Future)

```
Current (Development):
  localhost:3000 ←→ localhost:8000 ←→ Azure OpenAI
  (npm start)        (uvicorn)

Future (Production):
  Azure Static Web Apps    ←→    Azure App Service    ←→    Azure OpenAI
  (React SPA)                    (FastAPI Backend)
```

---

## Security Considerations

```
┌─────────────────┐
│  Azure Secrets  │
├─────────────────┤
│ • API Key       │
│ • Endpoint URL  │  ← Stored in backend/.env (not in git)
│ • Deployment ID │
└─────────────────┘
         │
         ↓ (Never exposed to client)
         │
  ┌──────────────┐
  │   Backend    │  ← Only backend accesses these
  ├──────────────┤
  │ Uses secrets │
  │ to call API  │
  └──────────────┘
         │
         ↓ (Only JSON responses sent to client)
         │
  ┌──────────────┐
  │   Frontend   │
  ├──────────────┤
  │ Calls backend│
  │ (no secrets) │
  └──────────────┘
```

**Key Points:**
- Secrets never in frontend code
- `.env` not committed to git
- `backend/.env.example` provided as template
- All API calls go through backend (no direct client→Azure)

---

## Testing Flow (Manual)

```
Backend Testing:
1. Start backend: ./start.sh
2. Test problem: curl http://localhost:8000/problem
3. Test analyze: curl -X POST http://localhost:8000/analyze \
                      -H "Content-Type: application/json" \
                      -d '{"code":"...","topic":"sliding_window"}'

Frontend Testing:
1. Start frontend: ./start.sh (includes frontend)
2. Open browser: http://localhost:3000
3. Test flow: Home → Interview → Submit code → Feedback

Integration Testing:
1. Both running: ./start.sh
2. Click "Start Mock Interview"
3. Submit code
4. Verify feedback appears
```

---

## Summary

**Architecture Pattern:** Classic Frontend-Backend-Cloud setup
- **Frontend:** Stateless SPA (React)
- **Backend:** Stateless API (FastAPI)
- **Cloud:** AI/ML service (Azure OpenAI)
- **Database:** None (MVP scope - hardcoded)

**Communication:** JSON over HTTP/HTTPS
- Frontend ↔ Backend: HTTP (localhost)
- Backend ↔ Azure: HTTPS (secure)

**Deployment:** Localhost development
- `./setup-env.sh` - Configure once
- `./start.sh` - Start anytime
- No database setup needed
- No Docker needed
- ~3 minutes to full working system
