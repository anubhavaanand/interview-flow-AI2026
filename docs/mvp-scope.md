# MVP Scope - interview-flow-AI2026

**Deadline**: 10 Jan 2026, 1:29 PM IST  
**Status**: Definition phase  
**Last Updated**: 9 Jan 2026

## What's INCLUDED in MVP

### A. Problem Serving (Backend)
- **Single hardcoded problem**: Sliding Window - "Maximum Sum Subarray of Size K"
- **GET /problem** endpoint returns:
  - Problem ID, title, description
  - Constraints and example
  - Function signature (Python)
  - Topic classification

### B. Code Analysis & Feedback (Backend + Azure OpenAI)
- **POST /analyze** endpoint accepts: `code` (string), `topic` (string)
- Calls Azure OpenAI with structured prompt
- Returns feedback covering:
  - ✅ Time complexity analysis
  - ✅ Space complexity analysis
  - ✅ Edge cases identification
  - ✅ Code quality observations
  - ✅ 3-step improvement plan

### C. Frontend Pages (Antigravity React)

#### Home (/)
- Project title
- Short description
- "Start Mock Interview" button → `/interview`

#### Interview (/interview)
- Problem statement display
- Code editor (textarea minimum, Monaco if time allows)
- Pre-filled function signature
- Submit button → POST to `/analyze`

#### Feedback (/feedback)
- Sectioned display of AI feedback
- Time/space complexity
- Edge cases and code quality
- 3-step improvement plan
- Navigation to Dashboard

#### Dashboard (/dashboard)
- Problems solved: "1/1"
- Weak topics: "Sliding Window"
- Readiness score: "Beginner"
- (Hardcoded for MVP)

## What's NOT Included (Non-Goals)

❌ Authentication/login system  
❌ Multiple problems or topics  
❌ Database or user history  
❌ Complex animations or advanced UI  
❌ Company-specific interview sets  
❌ Live video/voice interviews  
❌ User account persistence  

## Key Constraints

- **Language**: Python (backend), JavaScript/React (frontend)
- **AI Model**: GPT-4-turbo via Azure OpenAI
- **Deployment**: Works locally for MVP; can be demoed via local server
- **No external databases**: All data hardcoded
- **CORS**: Backend must accept frontend requests from localhost:3000

## Success Criteria for MVP

1. ✅ Full flow works end-to-end (Home → Interview → Submit → Feedback → Dashboard)
2. ✅ Backend GET /problem returns valid JSON
3. ✅ Backend POST /analyze calls Azure OpenAI and returns structured feedback
4. ✅ Frontend displays feedback in readable sections
5. ✅ No critical console errors
6. ✅ App runs on `localhost:3000` (frontend) + `localhost:8000` (backend)
7. ✅ Code pushed to GitHub (public repo)

## Timeline

- **Today (9 Jan)**: Backend + Frontend MVP complete, pushed to GitHub
- **Tonight**: Integration, polish, smoke testing
- **Morning (10 Jan)**: Final testing, pitch deck, video recording
- **Submission**: Before 1:29 PM IST, 10 Jan 2026
