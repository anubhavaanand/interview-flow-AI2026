# DEMO SCRIPT - Live Walkthrough (2 minutes)

## Pre-Demo Checklist
- [ ] Both services running: `./start.sh`
- [ ] Browser ready at http://localhost:3000
- [ ] Example code ready to paste (below)
- [ ] Zoom/screen recording set up
- [ ] Phone on silent
- [ ] Test mic/camera

---

## DEMO FLOW (2 minutes exactly)

### Part 1: Introduction (15 seconds)
**Say:** "I'm going to show you interview-flow-AI2026 in action. It's an AI-powered interview coach that gives real-time feedback on your coding solutions."

**Do:**
- Show blank desktop
- Click browser
- Navigate to http://localhost:3000

---

### Part 2: Home Page (10 seconds)
**Say:** "Here's our home page. Simple, clean design. All students need to do is click this button to start a mock interview."

**Do:**
- Show home page loads
- Pause 2 seconds for viewers to read
- Hover over "Start Mock Interview" button
- Click it

---

### Part 3: Problem Display (15 seconds)
**Say:** "And here's the problem. We start with a classic DSA problem: Maximum Sum Subarray. Students see the full description, constraints, an example with expected output, and a pre-filled function signature to help them get started."

**Do:**
- Let page load
- Scroll down to show full problem
- Pause 3 seconds to let judges read
- Click in code editor area

---

### Part 4: Code Submission (30 seconds)
**Say:** "Now I'll write a solution. Let me paste an example solution here..."

**Do:**
- Click in code textarea
- Clear any existing text
- Paste this solution:
```python
def maxSumSubarray(arr, k):
    if k > len(arr):
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Say:** "This is a sliding window solution. It's efficient, handles edge cases. Now let me submit it."

- Click Submit button
- Say: "Now watch as our AI analyzes this solution in real-time..."

---

### Part 5: AI Feedback (40 seconds)
**Say:** "And here's the magic - instant, comprehensive feedback from our AI system:"

**Do:**
- Wait for feedback page to load (5-10 seconds)
- Once loaded, scroll through and highlight:

**Time Complexity**
"First, time complexity analysis: This solution is O(n) - linear time, which is optimal for this problem. You can't do better than checking each element once."

**Space Complexity**
"Space complexity: O(1) - constant space. We're not using any extra space that grows with input size. Perfect!"

**Edge Cases**
"Edge cases identified: We handle when k > array length, empty arrays, single element, negative numbers. All covered!"

**Code Quality**
"Code quality: Good variable naming - window_sum is clear, max_sum is descriptive. We should add comments for clarity."

**Improvement Plan**
"And finally, three concrete improvement steps:
1. Add docstring explaining the algorithm
2. Add input validation at the start
3. Consider handling when k is 0 or negative

This is actionable feedback they can implement immediately."

- Pause 5 seconds for judges to read

---

### Part 6: Dashboard (10 seconds)
**Say:** "They can also view their dashboard showing progress across multiple problems and topics they're weak in."

**Do:**
- Scroll to navigation
- Click "Dashboard"
- Wait for load
- Show the stats briefly

**Say:** "This gives students a complete learning journey - not just one problem, but their whole interview prep progress."

---

### Part 7: Closing (20 seconds)
**Say:** "So that's interview-flow-AI2026. 
- Real problems
- Intelligent feedback
- Accessible globally
- Free and open-source

All built with modern tech: React frontend, FastAPI backend, and AI analysis via GitHub Models. This MVP took us just a few weeks to build, and we're ready to scale to help millions of students prepare for their interviews."

**Do:**
- Pause 3 seconds
- Say: "Any questions?"

---

## EXAMPLE CODE TO PASTE

```python
def maxSumSubarray(arr, k):
    if k > len(arr):
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

---

## ALTERNATIVE CODE (If you want to show "buggy" code first)

```python
def maxSumSubarray(arr, k):
    max_sum = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        max_sum = max(max_sum, current_sum)
    return max_sum
```

**This version:**
- Works but is O(n*k) instead of O(n)
- Doesn't handle edge cases
- Shows AI can identify optimization opportunities

**Then say:** "Let me show what happens if someone submits less optimal code..." [Submit this, show feedback, then go back and submit the optimized version]

---

## TIMING BREAKDOWN

```
Introduction:     15 sec ✓
Home Page:        10 sec ✓
Problem Display:  15 sec ✓
Code Input:       15 sec ✓
Submission:       10 sec ✓
Feedback Review:  40 sec ✓
Dashboard:        10 sec ✓
Closing:          20 sec ✓
────────────────────────
Total:           135 sec = 2 min 15 sec ✓
```

**Buffer:** If feedback takes longer (5-10 sec), you can skip dashboard section.

---

## CONTINGENCY PLANS

### If AI feedback doesn't load:
**Say:** "Let me try again - sometimes the AI takes a moment to process. While that loads, let me explain what you'd typically see here... [explain feedback components] And there it is!"

### If app crashes:
**Say:** "Let me restart the service - this is development mode after all. [Restart ./start.sh] The beauty of our setup is how easy it is to recover. [Reload page] And we're back!"

### If you run out of time:
**Cut to:** Skip dashboard, go straight to closing. Feedback is the critical part judges want to see.

### If asked about code quality:
**Response:** "This is MVP - we focused on core functionality. We'll add testing, CI/CD, better error handling in production. The foundation is solid."

---

## THINGS NOT TO SAY

❌ "Sorry it's slow"
❌ "Uh, let me try that again"
❌ "I'm not sure if this will work"
❌ "We only built this in a week"
❌ "It's just a prototype"

✅ Instead:
✅ "It's loading - great opportunity to explain the architecture"
✅ "Interesting - let me check this"
✅ "The system is designed to handle this"
✅ "We delivered a complete MVP in record time"
✅ "This is production-quality code"

---

## JUDGE REACTIONS & RESPONSES

**"How is this different from LeetCode?"**
"Great question! LeetCode shows solutions after you submit. We give personalized AI feedback on your specific code - what you did right, edge cases, complexity, and exactly how to improve. It's coaching, not just a problem bank."

**"How do you make money?"**
"MVP is free to build community. Premium features: interview prep courses, advanced problems, mentorship matching, B2B licensing to bootcamps. We expect 5% premium conversion = $50K+/month with 10K users."

**"What about plagiarism/cheating?"**
"Smart question. We can add code fingerprinting, test case validation, and interview style (live, timed). For now, the system is designed for honest self-improvement."

**"Why GitHub Models instead of Azure?"**
"Great call-out. Initially we planned Azure, but we wanted global accessibility and cost efficiency. GitHub Models gives us reliable AI, lower costs, and availability worldwide."

**"What's your competitive advantage?"**
"Three things: (1) Real-time personalized feedback, not just solutions, (2) Structured improvement plans, (3) Free tier removes price barriers. Most competitors charge $30-500/month."

---

## RECORDING TIPS

**Setup:**
- Use OBS or ScreenFlow
- Record at 1080p 30fps
- Mic: Use headset/external (better audio)
- Background: Clean desk or blurred
- Lighting: Good natural or ring light

**During Recording:**
- Speak clearly and slowly
- Pause after key points
- Let demos breathe (don't rush)
- Test audio/video before starting
- Have 2-3 takes ready

**Post-Recording:**
- Export as MP4
- Add intro (your name, project name, 5 sec)
- Add outro ("Questions? Contact me at...")
- Upload to YouTube unlisted
- Test playback before submitting

---

## SUBMISSION CHECKLIST

- [ ] Demo script memorized (or on phone to peek)
- [ ] Pitch deck created (PDF/PowerPoint)
- [ ] App running smoothly locally
- [ ] GitHub token in .env (don't commit .env!)
- [ ] Example code tested and working
- [ ] Demo video recorded and tested
- [ ] Pitch video recorded (3 min)
- [ ] Both videos uploaded or ready to upload
- [ ] Submission form filled out
- [ ] All files ready to submit
- [ ] 30 minutes before deadline, submit

---

