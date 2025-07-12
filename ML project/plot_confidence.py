import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
LOG_PATH = "output/log.txt"
PLOT_PATH = "output/confidence_plot.png"

# Read log file
df = pd.read_csv(LOG_PATH, sep="\t")

# Drop rows with no confidence (N/A)
df = df[df["Confidence"] != "N/A"].copy()
df["Confidence"] = df["Confidence"].astype(float)

# Plot
plt.figure(figsize=(12, 6))
for track_id, group in df.groupby("TrackID"):
    plt.plot(group["Frame"], group["Confidence"], label=f"ID {track_id}")

plt.title("Player Detection Confidence Over Time")
plt.xlabel("Frame")
plt.ylabel("Confidence")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig(PLOT_PATH)
plt.show()

print(f"[INFO] Plot saved to {PLOT_PATH}")
