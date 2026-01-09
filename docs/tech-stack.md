# Tech Stack - interview-flow-AI2026

**Project**: AI-powered DSA interview coach  
**Deadline**: 10 Jan 2026, 1:29 PM IST  

## Overview

```
┌─────────────────────────────────────────────────────────┐
│  Frontend (React/Antigravity)                           │
│  Pages: Home, Interview, Feedback, Dashboard            │
│  Port: localhost:3000                                   │
└─────────────────┬───────────────────────────────────────┘
                  │ (HTTP REST API)
┌─────────────────v───────────────────────────────────────┐
│  Backend (FastAPI)                                      │
│  GET /problem                                           │
│  POST /analyze → Azure OpenAI                           │
│  Port: localhost:8000                                   │
└─────────────────┬───────────────────────────────────────┘
                  │ (API calls)
┌─────────────────v───────────────────────────────────────┐
│  Azure OpenAI (GPT-4-turbo)                             │
│  Auth: AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT         │
└─────────────────────────────────────────────────────────┘
```

## Backend

### Framework & Language
- **Language**: Python 3.10+
- **Framework**: FastAPI (lightweight, async-capable)
- **Server**: Uvicorn (ASGI server)

### Key Dependencies
```
fastapi>=0.104.0
uvicorn>=0.24.0
openai>=1.0.0  # Azure OpenAI SDK
python-dotenv>=1.0.0  # Environment variables
pydantic>=2.0.0  # Data validation
```

### Project Structure
```
backend/
├── main.py                 # FastAPI app, routes
├── requirements.txt        # Dependencies
├── .env.example           # Template for secrets
└── prompts.py             # Azure OpenAI prompt templates
```

### Key Endpoints
| Method | Endpoint | Input | Output |
|--------|----------|-------|--------|
| GET | `/problem` | — | Problem JSON |
| POST | `/analyze` | `code`, `topic` | Structured feedback |
| GET | `/` | — | "API running" message |

### Environment Variables
```
AZURE_OPENAI_KEY=<your-key>
AZURE_OPENAI_ENDPOINT=<your-endpoint>
```

## Frontend

### Framework & Language
- **Language**: JavaScript (React)
- **Build Tool**: npm (Antigravity provides scaffold)
- **Routing**: React Router v6
- **HTTP Client**: Native `fetch()` API

### Key Dependencies
```
react>=18.0.0
react-router-dom>=6.0.0
(Monaco editor optional for advanced code editor, textarea OK for MVP)
```

### Project Structure
```
frontend/
├── src/
│   ├── App.jsx                    # Router setup
│   ├── pages/
│   │   ├── Home.jsx              # Landing page
│   │   ├── Interview.jsx         # Problem + editor
│   │   ├── Feedback.jsx          # AI feedback display
│   │   └── Dashboard.jsx         # Stats page
│   ├── components/               # Reusable components
│   │   ├── CodeEditor.jsx        # Text editor
│   │   ├── ProblemDisplay.jsx    # Problem rendering
│   │   └── FeedbackSection.jsx   # Feedback formatting
│   ├── api.js                    # Fetch wrapper
│   └── App.css                   # Minimal styling
├── public/
└── package.json
```

### Routes
| Path | Component | Purpose |
|------|-----------|---------|
| `/` | Home | Landing with start button |
| `/interview` | Interview | Problem + code editor |
| `/feedback` | Feedback | Display AI-generated feedback |
| `/dashboard` | Dashboard | Stats and progress |

## AI Services

### Azure OpenAI
- **Service**: Azure OpenAI API
- **Model**: GPT-4-turbo (or gpt-4 if turbo unavailable)
- **Temperature**: 0.7 (balanced)
- **Max Tokens**: 1000 (feedback response)
- **Endpoint**: Configured via `AZURE_OPENAI_ENDPOINT` env var
- **Authentication**: Key-based via `AZURE_OPENAI_KEY`

### Prompt Design
- **Location**: `backend/prompts.py`
- **Approach**: Provide code + topic, ask for structured feedback
- **Output Format**: JSON or plain text with clear sections
- **Safety**: No code execution—analysis only

## Development Tools

- **VS Code** with:
  - Azure OpenAI extension (for debugging API calls)
  - REST Client extension (for testing endpoints)
  - Python extension (backend development)
- **Postman** or `curl` (testing API endpoints)
- **Git**: Version control, GitHub repo

## Deployment (Optional for MVP)

### Option A: Local (Recommended for 48-hour MVP)
- Backend: `uvicorn main:app --reload` on port 8000
- Frontend: `npm start` on port 3000
- Demo via recorded video of local app running

### Option B: Azure (If time permits)
- **Backend**: Azure App Service or Azure Functions
- **Frontend**: Azure Static Web Apps
- **Storage**: Optional Azure Cosmos DB (not needed for MVP)

## CORS Configuration

### Backend (main.py)
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Dev
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Performance Targets

- **Problem Load**: < 100ms
- **Feedback Generation**: 5-15 seconds (Azure OpenAI latency)
- **Frontend Rendering**: < 500ms
- **No database queries** (in-memory hardcoded data)

## Security Considerations

- ✅ API keys stored in `.env`, not in code
- ✅ No user input execution (code analysis only, no eval())
- ✅ CORS restricted to localhost in dev
- ✅ Input validation on feedback endpoint
- ❌ No authentication needed for MVP

## Testing Strategy

- **Backend**: Manual curl/Postman tests
  - GET /problem returns valid JSON
  - POST /analyze with sample code returns feedback
- **Frontend**: Manual e2e testing
  - Home → Interview → Feedback → Dashboard flow
  - Console errors checked
- **Integration**: Full flow test with real Azure OpenAI call

## References

- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Router Docs](https://reactrouter.com)
- [Azure OpenAI Docs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Project Copilot Instructions](./../.github/copilot-instructions.md)
