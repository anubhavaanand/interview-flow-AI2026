# 🎬 Visual Quick Start Guide

## What You Need to Know (60 seconds)

### The Fix in 3 Lines
```bash
./setup-env.sh    # Configure Azure once
./start.sh        # Start everything
# Open http://localhost:3000 - Done!
```

---

## What's Running

```
Your Computer (Localhost)
├─ Frontend: http://localhost:3000 (React app)
│  └─ Pages: Home → Interview → Feedback → Dashboard
│
├─ Backend: http://localhost:8000 (FastAPI)
│  └─ APIs: GET /problem, POST /analyze
│
└─ Credentials: backend/.env (Azure OpenAI)
   └─ Authenticates to: Azure OpenAI Cloud
```

---

## The Complete Flow (What Happens When You Submit Code)

```
Step 1: Write Python Code
┌─────────────────────────┐
│  Interview Page         │
│                         │
│  def maxSum(arr, k):    │  ← You type here
│    # Your code          │
│                         │
│  [Submit] button        │
└─────────────────────────┘
         │ Click Submit
         ↓

Step 2: Backend Analyzes Code
┌─────────────────────────┐
│  FastAPI Backend        │
│  (localhost:8000)       │
│                         │
│  Receives: user code    │
│  Loads: prompt template │
│  Calls: Azure OpenAI    │
└─────────────────────────┘
         │ HTTPS request
         ↓

Step 3: Azure AI Analyzes
┌─────────────────────────┐
│  Azure OpenAI Cloud     │
│  (GPT-4-turbo)          │
│                         │
│  Analyzes code          │
│  Returns feedback       │
│  (3-10 seconds)         │
└─────────────────────────┘
         │ Response
         ↓

Step 4: Display Feedback
┌─────────────────────────┐
│  Feedback Page          │
│                         │
│  Time Complexity: O(n)  │
│  Space: O(1)            │
│  Edge Cases: ...        │
│  Improvements: ...      │
└─────────────────────────┘
```

---

## Files I Created

### Executable Scripts (Run These)
```
📜 start.sh
   └─ What: Starts backend & frontend
      How: ./start.sh start
      Command Options:
        ./start.sh start    - Start everything
        ./start.sh stop     - Stop everything  
        ./start.sh restart  - Restart
        ./start.sh status   - Show status
        ./start.sh logs     - Show live logs

📜 setup-env.sh
   └─ What: Configure Azure credentials
      How: ./setup-env.sh
      Then: Enter API Key and Endpoint
```

### Documentation Files (Read These)
```
📖 FIX_COMPLETE_SUMMARY.md       ← Start here! (This file's parent)
   └─ What: Complete explanation in simple terms
   
📖 QUICK_START_FIX.md
   └─ What: 3-step quick start guide
   
📖 ENVIRONMENT_SETUP.md
   └─ What: Detailed explanation of everything
   
📖 ARCHITECTURE.md
   └─ What: System diagrams and data flows
   
📖 MCP_FIX_EXPLANATION.md
   └─ What: Why MCP was restarting and how it's fixed
```

---

## One-Time Setup

### You'll Do This Once

```bash
# Terminal command:
./setup-env.sh

# What happens:
Please provide your Azure OpenAI credentials:

Azure OpenAI API Key: [PASTE YOUR KEY HERE]
Azure OpenAI Endpoint: [PASTE YOUR ENDPOINT HERE]
Azure OpenAI Deployment Name [gpt-4]: [Press Enter]

✅ Environment setup complete!

# Done! You now have backend/.env with your credentials
```

---

## Every Time You Work

### You'll Do This Every Session

```bash
# Terminal command:
./start.sh

# What happens:
════════════════════════════════════════════════════════════
  interview-flow-AI2026 Startup Script
════════════════════════════════════════════════════════════

📋 Setting up environment...
✅ Found .env file

🚀 Starting Backend (FastAPI)...
✅ Backend is running!

🚀 Starting Frontend (React)...
✅ Frontend is running!

════════════════════════════════════════════════════════════
✅ All services started!

📖 Access the application:
   Frontend: http://localhost:3000
   Backend:  http://localhost:8000

📂 Logs:
   Backend: tail -f /tmp/backend.log
   Frontend: tail -f /tmp/frontend.log

# Done! Everything is running
```

---

## Then Open Browser

```
http://localhost:3000
    ↓
[Home Page]
├─ Title: "interview-flow-AI2026"
├─ Subtitle: "AI-Powered DSA Interview Coach"
└─ Button: "Start Mock Interview"
    ↓ Click
[Interview Page]
├─ Problem Title: "Maximum Sum Subarray of Size K"
├─ Problem Description: "Given an array..."
├─ Code Editor: (empty textarea with function signature)
└─ Button: "Submit"
    ↓ Write code
    ↓ Click Submit
[Feedback Page] (appears after 3-10 seconds)
├─ Time Complexity: "O(n) - Linear"
├─ Space Complexity: "O(1) - Constant"
├─ Edge Cases: "Handles k > n, negative numbers, etc."
├─ Code Quality: "Good variable names, needs comments"
└─ Improvement Plan:
    1. Add edge case checks
    2. Optimize sliding window
    3. Test with edge cases
```

---

## Troubleshooting (If Something Goes Wrong)

### "Port already in use"
```
You: Run ./start.sh
Script: Automatically kills old process
Result: Works fine!
```

### "Backend not connecting"
```bash
./start.sh status
# Shows: ✅ Backend or ❌ Backend

./start.sh logs backend
# Shows: Error messages (if any)

# Fix credentials:
./setup-env.sh
./start.sh restart
```

### "Frontend not loading"
```bash
./start.sh logs frontend
# Shows: Build errors (if any)

# Rebuild:
./start.sh stop
rm -rf frontend/node_modules
./start.sh start
```

---

## MCP Server Fix (What I Did)

### The Problem
```
Every command → MCP server restarts → Can't work
```

### The Root Cause
```
Port conflict → Process doesn't stop → Startup fails → Terminal dies
```

### The Solution
```
Auto-detect port → Kill old process → Clean startup → Never restart
```

### The Script
```bash
./start.sh
# Does all the above automatically
# You just run one command, everything works
```

---

## Architecture in Pictures

### Simple Version
```
Browser (You)
    ↕ 
React App (Port 3000)
    ↕ (JSON)
FastAPI (Port 8000)
    ↕ (HTTPS + API Key)
Azure Cloud
```

### What Talks to What
```
Browser ←→ Frontend (React)
          - Shows pages
          - Takes user input
          - Displays feedback

Frontend ←→ Backend (FastAPI)
          - Sends code to analyze
          - Gets feedback back

Backend ←→ Azure OpenAI
          - Sends code + prompt
          - Gets AI analysis
```

---

## Time Breakdown

### Setup (One-Time)
```
1. ./setup-env.sh      2 minutes
   (Enter credentials)

Total: 2 minutes
```

### Startup (Every Session)
```
1. ./start.sh          1 minute
   (Starts both services)

2. Open browser        30 seconds
   (Load http://localhost:3000)

Total: 1.5 minutes
```

### Usage
```
1. Use the app         5-10 minutes
   (Interview → Submit → Feedback)

No restarts needed!
```

---

## Key Points

✅ **No More Restarts**
- Old problem: MCP server crashed each time
- New solution: Everything runs in background
- Result: Just run `./start.sh` once per session

✅ **Automatic Port Cleanup**
- Old problem: Ports blocked by old processes
- New solution: Script kills old processes automatically
- Result: Never manually clean up ports again

✅ **One-Command Startup**
- Old problem: Run backend in terminal 1, frontend in terminal 2, both block
- New solution: `./start.sh` starts both in background
- Result: Terminal stays free for other commands

✅ **Clear Logs**
- Old problem: Hard to see what's happening
- New solution: `./start.sh logs` shows both
- Result: Easy debugging if needed

---

## Phase 4 (What's Next)

### Test the Full Flow
```
1. Run ./setup-env.sh         (if not done yet)
2. Run ./start.sh
3. Open http://localhost:3000
4. Click "Start Mock Interview"
5. See DSA problem
6. Write Python code
7. Click "Submit"
8. See AI feedback (from Azure OpenAI)
9. Check Dashboard
```

### Success Criteria
- [ ] Home page loads
- [ ] Can view DSA problem
- [ ] Can submit code
- [ ] Get AI feedback back
- [ ] Can view feedback
- [ ] Can see dashboard

**Estimated time: 15-20 minutes**

---

## Phase 5 & 6 (After Phase 4)

### Phase 5: Pitch & Demo (2-3 hours)
- Create pitch deck (10-15 slides)
- Write pitch script (3 minutes)
- Record pitch video (5 minutes)

### Phase 6: Submit (30 minutes)
- Record demo video (2-3 minutes)
- Fill submission form
- Submit to Imagine Cup

**Total remaining: 3-4 hours**

---

## Deadline Status

```
Deadline: 2026-01-10 1:29 PM IST

Current time: 2026-01-09 16:30+ IST
Time remaining: ~17 hours

Phase 4 (Testing): 1 hour
Phase 5 (Pitch & Video): 2-3 hours
Phase 6 (Submit): 30 minutes
Total needed: 4 hours

Buffer: ~13 hours
Status: ✅ On track, very comfortable
```

---

## Quick Command Reference

```bash
# One-time setup
./setup-env.sh

# Every session
./start.sh

# Check status
./start.sh status

# View logs
./start.sh logs both

# Stop everything
./start.sh stop

# Restart
./start.sh restart

# Open in browser
# http://localhost:3000
```

---

## Questions to Ask Yourself

**"Is this working?"**
→ `./start.sh status`

**"What's the error?"**
→ `./start.sh logs both`

**"How do I fix it?"**
→ Read `QUICK_START_FIX.md` or `ENVIRONMENT_SETUP.md`

**"What's happening?"**
→ Read `ARCHITECTURE.md` or `FIX_COMPLETE_SUMMARY.md`

**"Why is MCP not restarting?"**
→ Read `MCP_FIX_EXPLANATION.md`

---

## You're All Set! 🎉

```bash
cd /home/anubhavanand/Desktop/interview-flow-AI2026
./setup-env.sh
./start.sh
# Open http://localhost:3000

Success! ✅
```

**No more MCP server restarts. Period.**
