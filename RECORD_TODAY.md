# QUICK REFERENCE: VIDEO RECORDING TODAY

## ⏱️ TIMELINE (Do This NOW)

```
4:00 PM: Start recording environment setup
4:30 PM: Record Demo Video (Product Demo Script)
5:00 PM: Record Pitch Video (Pitch Script)
5:30 PM: Edit and upload to YouTube
6:00 PM: Get YouTube links
6:30 PM: Fill submission form (draft)
```

---

## 🎬 DEMO VIDEO (2:30-3:00 min)

**What to Show:**
1. Home page → "Start Mock Interview" button
2. Interview page → DSA problem displayed
3. Code editor → Paste solution (pre-written: O(n*k) solution)
4. Submit button → Watch it load
5. Feedback page → Point out each section:
   - Time Complexity: "O(n*k) - can optimize to O(n)"
   - Space Complexity: "O(1) - good"
   - Edge Cases: "Missing k > n, empty array, k = 0"
   - Code Quality: "Add docstring and type hints"
   - 3-Step Plan: "Validate input → sliding window → edge cases"
6. Dashboard page → Show stats
7. Close with: "That's interview-flow. AI coach for DSA interviews."

**Script**: [Full script in DEMO_VIDEOS.md](DEMO_VIDEOS.md)

**What You Need:**
- [ ] Browser with localhost:3000 open
- [ ] Code ready to paste (copy from below)
- [ ] Microphone (USB or builtin)
- [ ] Screen recording tool (OBS/ScreenFlow/Loom)
- [ ] Good lighting

**Code to Paste:**
```python
def maxSumSubarray(arr, k):
    max_sum = 0
    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    return max_sum
```

**After Recording:**
- Edit: Add 3-sec intro card, trim silence, add captions
- Upload: To YouTube (unlisted)
- Copy link: `https://youtube.com/watch?v=...`

---

## 🎤 PITCH VIDEO (1:30-2:00 min)

**Key Points (Memorize or Read):**
1. Problem hook: "85% of students fail technical interviews"
2. Solution: "We built interview-flow - AI coach for code feedback"
3. Market: "3.5M students, $2B+ opportunity"
4. Proof: "Working MVP, built in 24 hours"
5. Business: "Freemium: $4.99/month, hit $250K MRR by month 6"
6. Vision: "Help 1M+ students ace their dream job"

**Full Script**: [PITCH_DECK.md](PITCH_DECK.md) - "3-Minute Pitch" section

**What You Need:**
- [ ] Camera (phone is fine) or webcam
- [ ] Script printed or on another monitor
- [ ] Good lighting (natural window light)
- [ ] Quiet room
- [ ] Microphone

**Recording Tips:**
- Speak clearly, not too fast
- Make eye contact with camera
- Show genuine passion
- Do 2-3 takes, pick the best
- Keep it natural (not robotic)

**After Recording:**
- Edit: Add intro, add product screenshots (optional)
- Upload: To YouTube (unlisted)
- Copy link: `https://youtube.com/watch?v=...`

---

## ✅ SERVICES RUNNING CHECK

Before you record, verify both are up:

```bash
# Check backend
curl http://localhost:8000
# Should return: {"status":"ok","message":"..."}

# Check frontend
curl http://localhost:3000 | grep "<title>"
# Should return: <title>React App</title>
```

If not running, start them:
```bash
./start.sh
# Wait for: "Frontend compiled successfully"
```

---

## 📹 RECORDING TOOLS

**Free Options:**
- **Mac:** QuickTime (built-in), ScreenFlow free trial
- **Windows:** OBS Studio (free, professional)
- **Online:** Loom (free tier), YouTube Live (direct)
- **All:** CapCut (free editor)

**Recommended Setup:**
1. **Recording:** OBS Studio (free, works on all platforms)
2. **Editing:** CapCut (free, easy, good results)
3. **Upload:** YouTube unlisted link

---

## 🎯 YOUTUBE UPLOAD SETTINGS

When uploading, use these settings:

```
Title: "interview-flow-AI2026: Demo" (or "Pitch")
Description: [Link to GitHub repo]
Visibility: Unlisted (not public, not private)
Category: Science & Technology
Allow comments: Yes
Allow embedding: Yes
```

---

## 🚀 WHAT HAPPENS NEXT

1. **Today (4:00-6:30 PM):** Record both videos, upload to YouTube
2. **Tomorrow AM (9:00-10:00 AM):** Get YouTube links, fill Imagine Cup form
3. **Tomorrow (1:00 PM):** Hit submit button
4. **Tomorrow (1:29 PM):** 🎉 DEADLINE HITS, celebration begins!

---

## 💡 FINAL REMINDERS

- **Keep it simple:** No fancy effects, just clear demo + pitch
- **Test everything:** Videos must play smoothly
- **Audio quality:** Clear voice matters more than video
- **Speak with confidence:** You built something real in 24 hours!
- **Don't overthink:** First good take is good enough

---

## 📋 SUBMISSION FORM FIELDS

You'll fill these tomorrow AM:

```
Team Name: [Your Name]
Project: interview-flow-AI2026
Category: AI & Machine Learning
Demo Video Link: [YouTube from step 1]
Pitch Video Link: [YouTube from step 2]
GitHub: https://github.com/anubhavaanand/interview-flow-AI2026
Description: [Copy from PITCH_DECK.md or below]
```

**One-Liner for Form:**
"AI coach that helps students ace technical interviews by analyzing their code in real-time and providing personalized feedback on complexity, edge cases, and improvements."

---

## 🏁 FINAL CHECKLIST

Before you hit record:

- [ ] Services running? (Backend 8000, Frontend 3000)
- [ ] Code ready to paste? (copied to clipboard)
- [ ] Mic working? (test in settings)
- [ ] Lighting good? (face or screen clearly visible)
- [ ] Room quiet? (no background noise)
- [ ] Recording tool open? (OBS or ScreenFlow)
- [ ] YouTube account ready? (can upload)
- [ ] Time blocked? (2-3 hours uninterrupted)

**READY? HIT RECORD.** 🎬

---

**Status: READY FOR VIDEO PRODUCTION**  
**Next Action: Open recording tool and start!**
