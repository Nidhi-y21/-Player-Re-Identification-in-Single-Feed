# -Player-Re-Identification-in-Single-Feed
📋 Overview
This project implements player re-identification and tracking in a single video feed.
Players are detected in each frame, and those who leave and later re-enter the frame are assigned the same unique identity (ID).

This submission solves the single-feed re-identification task as per the assignment.

📂 Output Files
📹 Output Video: output/output_video.mp4 — video with bounding boxes & IDs

📄 Log File: output/log.txt — frame-by-frame record of IDs & confidence

📊 Confidence Plot: output/confidence_plot.png — visualization of confidence over time

🚀 How to Run
🧰 Setup
1️⃣ Clone the repository:

bash
Copy
Edit
git clone <https://github.com/Nidhi-y21/-Player-Re-Identification-in-Single-Feed>
cd <repo-folder>
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Place the following files in the repo folder:

Provided YOLOv11 model: yolov11.pt

Provided video: 15sec_input_720p.mp4

🧑‍💻 Run the pipeline:
bash
Copy
Edit
python main.py
Output files will be saved in the output/ folder.

📈 Optional: Generate Confidence Plot
After running main.py, run:

bash
Copy
Edit
python plot_confidence.py
This produces:
output/confidence_plot.png

📝 Approach
✅ Detection: YOLOv11 (provided)
✅ Tracking & Re-ID: DeepSORT
✅ Tuned parameters to balance recall & precision
✅ Outputs include video, log, and plot for analysis

📊 Sample Outputs
Output	Screenshot
🎥 Video	output/output_video.mp4 (IDs drawn on players)
📄 Log	output/log.txt (Frame, TrackID, Confidence)
📈 Plot	output/confidence_plot.png

🧪 Notes
Confidence threshold was tuned to 0.3 to minimize false positives.

DeepSORT tracker parameters adjusted to handle occlusions & re-entries.

Log & plot help analyze detection confidence trends.

🤝 Credits
YOLOv11 model: [provided in assignment]

DeepSORT: https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch

Author: Nidhi
