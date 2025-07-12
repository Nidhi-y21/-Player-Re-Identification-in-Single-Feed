import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import os

# Paths
VIDEO_PATH = "15sec_input_720p.mp4"
MODEL_PATH = "yolov11.pt"
OUTPUT_VIDEO_PATH = "output/output_video.mp4"
LOG_PATH = "output/log.txt"

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Load YOLOv11
print("[INFO] Loading YOLOv11 model...")
model = YOLO(MODEL_PATH)

# Initialize DeepSORT tracker with tuned parameters
print("[INFO] Initializing DeepSORT tracker...")
tracker = DeepSort(
    max_age=50,
    n_init=2,
    max_iou_distance=0.9,
)

# Read input video
cap = cv2.VideoCapture(VIDEO_PATH)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Open log file
log_file = open(LOG_PATH, "w")
log_file.write("Frame\tTrackID\tConfidence\n")

frame_num = 0

print("[INFO] Starting processing...")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_num += 1

    # Run YOLOv11 detection with tuned confidence threshold
    results = model(frame, conf=0.3)
    detections = results[0].boxes.xyxy.cpu().numpy()
    confidences = results[0].boxes.conf.cpu().numpy()
    class_ids = results[0].boxes.cls.cpu().numpy()

    # Filter only player detections
    det_list = []
    for det, conf, cls_id in zip(detections, confidences, class_ids):
        if int(cls_id) == 0:
            x1, y1, x2, y2 = det
            det_list.append(([x1, y1, x2 - x1, y2 - y1], conf, 'player'))

    # Update tracker
    tracks = tracker.update_tracks(det_list, frame=frame)

    # Draw and log results
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = track.to_ltrb()
        l, t, r, b = int(l), int(t), int(r), int(b)

        # Find matching detection confidence
        conf = None
        for det, dconf, cls in det_list:
            dx, dy, dw, dh = det
            if abs(l - dx) < 10 and abs(t - dy) < 10:
                conf = dconf
                break

        label = f"ID:{track_id}"
        if conf:
            label += f" ({conf:.2f})"
            log_file.write(f"{frame_num}\t{track_id}\t{conf:.2f}\n")
        else:
            log_file.write(f"{frame_num}\t{track_id}\tN/A\n")

        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, label, (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    out.write(frame)

    if frame_num % 10 == 0:
        print(f"[INFO] Processed {frame_num} frames...")

cap.release()
out.release()
log_file.close()
print(f"[INFO] Done. Output saved to {OUTPUT_VIDEO_PATH}")
print(f"[INFO] Log saved to {LOG_PATH}")
