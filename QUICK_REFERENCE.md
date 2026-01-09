# Quick Reference - interview-flow-AI2026

## 🚀 Current Status
- ✅ Phases 1-3 Complete: Full MVP running locally
- 🔋 Backend: http://localhost:8000 (FastAPI)
- 🎨 Frontend: http://localhost:3000 (React)
- ⏳ Phases 4-6: Integration, Polish, Pitch, Recording, Submission

---

## 🔑 Azure OpenAI Setup (CRITICAL NEXT STEP)

```bash
# Set credentials (one-time in terminal session)
export AZURE_OPENAI_KEY="<your-api-key>"
export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com/"

# Verify they're set
echo $AZURE_OPENAI_KEY
echo $AZURE_OPENAI_ENDPOINT
```

Then restart backend:
```bash
cd backend
pkill -f uvicorn  # Kill existing process
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🧪 Testing Checklist

### Backend Testing
```bash
# Test health
curl http://localhost:8000/

# Test /problem endpoint
curl http://localhost:8000/problem | jq .

# Test /analyze endpoint (after credentials set)
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "code":"def maxSum(arr, k):\n    return max(sum(arr[i:i+k]) for i in range(len(arr)-k+1))",
    "topic":"sliding_window"
  }'
```

### Frontend Testing
1. Open http://localhost:3000
2. Click "Start Mock Interview" → should go to /interview
3. Should see Sliding Window problem loaded
4. Enter some code in editor
5. Click "Submit for Analysis" → should post to backend
6. Should navigate to /feedback (check browser console for errors)
7. Click "View Dashboard" → should show stats page

---

## 📊 Key Files

| File | Purpose | Status |
|------|---------|--------|
| `backend/main.py` | FastAPI app | ✅ Complete |
| `backend/prompts.py` | Azure OpenAI prompt | ✅ Complete |
| `frontend/src/api.js` | API service | ✅ Complete |
| `frontend/src/pages/*` | React pages | ✅ Complete |
| `.github/copilot-instructions.md` | AI agent guide | ✅ Complete |
| `docs/mvp-scope.md` | MVP requirements | ✅ Complete |
| `docs/tech-stack.md` | Tech details | ✅ Complete |

---

## 🐛 Common Issues & Fixes

### Frontend can't reach backend
```
Error: "Failed to load problem"
Fix: Check backend is running on port 8000
     Verify CORS is enabled in main.py
```

### Azure OpenAI "Missing credentials"
```
Error: "OpenAIError: Missing credentials"
Fix: 1. Set AZURE_OPENAI_KEY env var
     2. Set AZURE_OPENAI_ENDPOINT env var
     3. Restart backend (kill + restart uvicorn)
```

### Port already in use
```
Error: "Address already in use"
Fix: Kill the process:
     lsof -i :8000     # Find process
     kill -9 <PID>     # Kill it
     Then restart
```

---

## 📋 Phase 4 Checklist

- [ ] Azure OpenAI credentials set and verified
- [ ] `/analyze` endpoint tested with real API call
- [ ] Full flow tested (Home → Interview → Feedback → Dashboard)
- [ ] No console errors in frontend
- [ ] No errors in backend logs
- [ ] Error messages display properly if API fails
- [ ] UI looks presentable (minimal polish needed)
- [ ] Code pushed to GitHub

---

## ⏰ Timeline Remaining

| Phase | Time | Deadline | Status |
|-------|------|----------|--------|
| 4. Integration | 3h | 10 PM - 12 AM IST | ⏳ Current |
| 5. Pitch Deck | 3h | 12 AM - 3 AM IST | ⏳ Next |
| 6. Recording | 2h | 8 AM - 1:29 PM IST | ⏳ Tomorrow |

**Total buffer: ~3-4 hours** (ahead of schedule)

---

## 📌 Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# Add and commit
git add -A
git commit -m "Your message"

# Push to GitHub
git push origin main

# View remote
git remote -v
```

---

## 🎯 Success Criteria

✅ Backend MVP - Complete
✅ Frontend MVP - Complete  
⏳ Full end-to-end flow working
⏳ Pitch deck created
⏳ Videos recorded
⏳ Form submitted before 1:29 PM IST on 10 Jan

---

## 💬 Quick Contacts

- Azure OpenAI: https://portal.azure.com
- GitHub Repo: https://github.com/anubhavaanand/interview-flow-AI2026
- Imagine Cup: https://imaginecup.microsoft.com

---

**Last Updated**: 9 Jan 2026, after Phase 3 completion
**Next Review**: After Phase 4 integration testing
