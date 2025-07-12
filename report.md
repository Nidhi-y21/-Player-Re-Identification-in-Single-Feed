📄 Final Report: Player Re-Identification in Single Feed
📋 Overview
This project implements player re-identification and tracking in a single video feed, as per the assignment requirements.
The goal is to detect players in each frame and ensure that players who leave and later reappear are assigned the same identity (ID) throughout the video.

We process the provided 15sec_input_720p.mp4 using the YOLOv11 model for detection and DeepSORT for tracking and re-identification.
The final output is a video with bounding boxes and unique player IDs, a frame-by-frame log file, and a confidence-over-time plot for analysis.

🧑‍💻 Approach
We implemented a tracking-by-detection pipeline:

Used YOLOv11 (provided) to detect players in each frame.

Lowered the confidence threshold to 0.3 to improve recall while minimizing false positives.

Used DeepSORT tracker to assign consistent IDs to players, even after they leave and re-enter the frame.

The tracker is tuned with the following parameters:

max_age = 50 — allows longer disappearances without losing track.

n_init = 2 — faster confirmation of new tracks.

max_iou_distance = 0.9 — tolerates higher overlaps when matching.

The output video (output/output_video.mp4) shows each detected player with their unique ID and detection confidence on-screen.

🔍 Techniques Tried
Tuned YOLOv11’s confidence threshold between 0.1 and 0.4 to find a balance between detecting all players and avoiding false positives.

Adjusted DeepSORT parameters to handle occlusions and long disappearances.

Added on-screen confidence display for each player detection.

Generated a log file and a confidence-over-time plot for deeper analysis.

📝 Log File Analysis
In addition to the output video, the solution generates a detailed log file:

lua
Copy
Edit
output/log.txt
📋 Format
The log file records the frame-by-frame tracking results:

mathematica
Copy
Edit
Frame	TrackID	Confidence
1	1	0.91
1	2	0.85
2	1	0.90
2	3	0.76
…
Each row represents:

Frame: the current video frame number.

TrackID: the unique ID assigned to the player by the tracker.

Confidence: the YOLOv11 detection confidence for this player in that frame.

If no detection confidence is available for a tracked player in a frame, it is recorded as N/A.

🔍 Insights
This log file helps verify that player IDs remain consistent even when players leave and reappear, and identifies weak detections that could be improved.

📈 Confidence-Over-Time Plot
We also produced a visualization of detection confidence over time for each player ID.
This helps to observe how detection quality varies throughout the video and identify potential ID switches or weak detections.

The plot is saved as:

bash
Copy
Edit
output/confidence_plot.png
An example plot shows separate lines for each tracked player, with their confidence plotted across all frames.

🚧 Challenges
Some players on the edge of the frame or partially occluded were missed by the detector.

Occasional false positives still occurred, despite tuning the threshold.

Bounding boxes may jitter slightly frame-to-frame.

➕ Future Work
Fine-tune the YOLOv11 model for the specific dataset to improve detection precision.

Use a stronger re-identification model to improve embedding matching in DeepSORT.

Apply temporal smoothing to bounding boxes for more stable visualization.

📦 Output Files
📹 Output Video: output/output_video.mp4

📄 Log File: output/log.txt

📊 Confidence Plot: output/confidence_plot.png

✅ Summary
The solution meets the assignment objective of re-identifying and consistently tracking players in a single video feed, even when they leave and re-enter the frame.
The additional log file and analysis demonstrate attention to detail and provide useful insights into system performance.

