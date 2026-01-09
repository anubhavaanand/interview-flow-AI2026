# Copilot Instructions for interview-flow-AI2026

## Project Overview
**interview-flow-AI2026** is an AI-powered DSA interview coach that helps students practice coding interviews with realistic problems and personalized feedback powered by Azure OpenAI.

**Critical Context**: MVP submission deadline is **10 Jan 2026, 1:29 PM IST**. This is a high-velocity project—focus on done-is-better-than-perfect MVP completion.

## Architecture & Key Components

### High-Level Flow
```
User → Frontend (Antigravity/React) → Backend (FastAPI) → Azure OpenAI → Feedback Response
```

### Core Components
1. **Frontend** (Antigravity React app)
   - `/ (Home)` – Title + "Start Mock Interview" button
   - `/interview` – Problem display + Monaco code editor + Submit button
   - `/feedback` – AI-generated feedback (complexity, edge cases, improvement plan)
   - `/dashboard` – Hardcoded stats (problems solved, weak topics, readiness score)

2. **Backend** (FastAPI Python)
   - `GET /problem` – Returns hard-coded DSA problem JSON (Sliding Window example)
   - `POST /analyze` – Accepts code + topic, calls Azure OpenAI, returns structured feedback
   - Prompt design is critical: must ask for time/space complexity, edge cases, code quality, 3-step plan

3. **AI Integration** (Azure OpenAI)
   - Model: GPT-4-turbo (or available equivalent)
   - Single critical prompt for code feedback
   - Must handle user code safely (no execution risk)

## Critical Developer Workflows

### Local Setup & Build

**Backend (FastAPI)**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
export AZURE_OPENAI_KEY=<your-key>
export AZURE_OPENAI_ENDPOINT=<your-endpoint>
uvicorn main:app --reload  # Runs on http://localhost:8000
```

**Frontend (Antigravity React)**
```bash
cd frontend
npm install  # or yarn install
npm start    # Runs on http://localhost:3000
```

### Testing & Validation
- **Backend**: No automated tests required for MVP. Test manually:
  - `curl http://localhost:8000/problem` → verify JSON structure
  - POST to `/analyze` with sample code + topic → verify feedback quality in response
- **Frontend**: Manual e2e testing only
  - Home → Interview → Submit code → Feedback loads → Dashboard
  - No broken links in navigation; console errors must be fixed before submission
- **AI Integration**: Always test feedback quality with different code samples (working, buggy, inefficient)

### Deployment (For Imagine Cup)
- **Option A (Recommended for time)**: Record demo video with app running locally
- **Option B (If time allows)**: Deploy backend to Azure App Service / Azure Functions, frontend to Azure Static Web Apps
- **CORS**: Backend must allow requests from frontend URL (localhost:3000 for dev, Azure domain in prod)

## Project-Specific Conventions

### Code Style & Patterns

**Backend (FastAPI)**
- Use type hints for all functions: `def analyze(code: str, topic: str) -> dict:`
- Return JSON responses consistently: `{"success": bool, "data": {...}, "error": str or null}`
- Environment variables for secrets (AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT)
- Error handling: Catch Azure OpenAI API errors gracefully, return meaningful messages to frontend

**Frontend (React/Antigravity)**
- Functional components with hooks (useState, useEffect)
- Navigation: use React Router for `/`, `/interview`, `/feedback`, `/dashboard`
- API calls: Use `fetch()` with try/catch; store responses in state
- State management: Keep it simple—no Redux needed for MVP scope

### File Organization

```
backend/
├── main.py              # FastAPI app, routes for /problem and /analyze
├── requirements.txt     # Python dependencies
└── prompts.py          # Azure OpenAI prompt templates (CRITICAL)

frontend/
├── src/
│   ├── App.jsx          # Router setup
│   ├── pages/
│   │   ├── Home.jsx
│   │   ├── Interview.jsx
│   │   ├── Feedback.jsx
│   │   └── Dashboard.jsx
│   ├── components/      # Reusable components (CodeEditor, ProblemDisplay, etc.)
│   └── api.js          # Fetch wrapper for backend calls
└── package.json
```

### Critical Patterns

**Problem Data Structure** (backend `/problem` response):
```json
{
  "id": "sliding_window_1",
  "title": "Maximum Sum Subarray of Size K",
  "description": "Given an array of integers and a number k, find the maximum sum of any subarray of size k.",
  "constraints": "1 <= k <= n, -1000 <= array[i] <= 1000",
  "example": "Input: [2, 1, 5, 1, 3, 2], k=3. Output: 9 (subarray [5, 1, 3])",
  "topic": "sliding_window",
  "function_signature": "def maxSumSubarray(arr, k):\n    pass"
}
```

**Feedback Data Structure** (backend `/analyze` response):
```json
{
  "success": true,
  "feedback": {
    "time_complexity": "O(n) solution is optimal",
    "space_complexity": "O(1) extra space needed",
    "edge_cases": "Handles k > n? Input validation needed.",
    "code_quality": "Variable names are clear. Consider adding comments.",
    "improvement_plan": [
      "Step 1: Add edge case checks at function start",
      "Step 2: Optimize to single-pass sliding window",
      "Step 3: Test with negative numbers and k=1"
    ]
  }
}
```

**Azure OpenAI Prompt** (in `prompts.py`):
- Must request structured feedback (complexity, edge cases, improvements)
- Include the user's code in context but DON'T execute it
- Always return actionable 3-step improvement plan
- Keep feedback under ~500 tokens to avoid timeout

## Integration Points & Dependencies

**Azure OpenAI Integration**
- Service: Azure OpenAI API
- Authentication: Bearer token in header from AZURE_OPENAI_KEY
- Endpoint: Configured via AZURE_OPENAI_ENDPOINT env var
- Model: GPT-4-turbo (check Azure console for available models)
- **Critical**: Test locally with valid credentials before committing

**Frontend ↔ Backend Communication**
- Backend runs on `http://localhost:8000`
- Frontend CORS: Backend must include `Allow-Origin: http://localhost:3000` in dev
- All requests use `Content-Type: application/json`
- Frontend stores feedback in state, not persisted to DB (OK for MVP)

**Dependencies**
- **Backend**: `fastapi`, `uvicorn`, `openai` (Azure OpenAI SDK), `python-dotenv`
- **Frontend**: `react`, `react-router-dom`, `axios` or native `fetch` (no third-party editor; plain textarea is OK, Monaco optional)
- **No database required for MVP** (hardcoded problem + ephemeral feedback)

## Common Tasks for AI Agents

### Adding a New Problem (After MVP)
- Add entry to hardcoded problem list in `backend/main.py` following the Problem Data Structure
- Test `/problem?id=new_id` endpoint
- Update frontend problem selector (when UI supports multiple problems)

### Improving Feedback Quality
- Edit the prompt template in `backend/prompts.py`
- Test with POST `/analyze` in Postman with sample buggy code
- Iterate prompt to get clearer, more actionable feedback
- Keep response under ~500 tokens for latency

### Debugging Integration Issues
- **Backend fails**: Check AZURE_OPENAI_KEY and AZURE_OPENAI_ENDPOINT env vars are set
- **Frontend won't load feedback**: Check browser console for CORS errors; verify backend `/analyze` is responding with expected JSON
- **Slow feedback**: Check Azure OpenAI quota and model availability; may need to request higher limits

### Fixing Frontend Layout
- All pages in `frontend/src/pages/` use React hooks
- State passed down or stored via Context API (no Redux—too slow to implement)
- CSS: Use inline styles or simple CSS modules; keep styling minimal (MVP doesn't need polish)

## References

- **README.md**: Project overview and quick start
- **.gitignore**: Files excluded from version control
- **package.json** / **requirements.txt** / **pom.xml**: Dependency management

---

**Last Updated**: January 9, 2026  
**Status**: Initial template - awaiting codebase initialization
