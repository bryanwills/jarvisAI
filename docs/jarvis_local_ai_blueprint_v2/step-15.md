# Step 15 — Real-time Focus Coach
**Goal:** Gentle nudges without heavy GPU.

## Rules
- Off-task > N minutes (YouTube/social during focus) → notify.  
- Idle > 20 min during planned block → check-in.  
- Last meal > 4 hours → suggest snack/water.

## Implementation
- Daemon reads ActivityWatch live API every 5 minutes.  
- Sends notifications (macOS `osascript` or a tiny menu-bar app).  
- Logs nudges to `events` for weekly review.
