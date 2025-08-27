# Step 19 — Image/Video Generation (StabilityMatrix/LykosAI)
**Goal:** Local creative workflows.

## Docker Compose (GPU)
- Follow StabilityMatrix docs; store models on NVMe.  
- Expose an HTTP endpoint for “recipe→video” tool.

## Workflow
1. Parse recipe → steps.  
2. Generate step images/clips (txt2img/img2img).  
3. Stitch with FFmpeg; add TTS voiceover.  
4. Return video URL/path; store in DB; optionally publish via n8n.
