# interview-flow-AI2026

AI-powered DSA interview coach for coding interview preparation.

## 🎯 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- Azure OpenAI API key and endpoint

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables
export AZURE_OPENAI_KEY="your-key"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"

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
# Test GET /problem
curl http://localhost:8000/problem | jq

# Test POST /analyze
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"code":"def f():\n  pass","topic":"sliding_window"}'
```

### Frontend
- Open http://localhost:3000
- Test full flow: Home → Interview → Feedback → Dashboard

## 📚 Documentation

- [MVP Scope](docs/mvp-scope.md) - Feature requirements
- [Tech Stack](docs/tech-stack.md) - Technology details
- [Copilot Instructions](.github/copilot-instructions.md) - AI agent guide
- [Frontend README](frontend/README.md) - React app details

## 🤝 Contributing

This is an MVP for Imagine Cup 2026. All development follows the [Copilot Instructions](.github/copilot-instructions.md).

## 📄 License

This project is part of the Imagine Cup 2026 submission.

---

**Deadline**: 10 Jan 2026, 1:29 PM IST  
**Status**: Phase 3 Complete (Frontend MVP Running)
