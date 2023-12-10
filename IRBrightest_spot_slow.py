import cv2
import numpy as np

# Re-initializing the path to the video file
video_path = 'Resources/video_2023-12-09_18-13-38.mp4'

# Function to find the brightest spot in the frame
def find_brightest_spot(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    return maxLoc

# Function to draw a green square around the brightest spot
def draw_green_square(frame, center, size=20):
    top_left = (max(center[0] - size, 0), max(center[1] - size, 0))
    bottom_right = (min(center[0] + size, frame.shape[1]), min(center[1] + size, frame.shape[0]))
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    return frame

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Create a window to display the frames
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Find the brightest spot
    brightest_spot = find_brightest_spot(frame)

    # Draw the green square
    frame_with_square = draw_green_square(frame, brightest_spot)

    # Display the frame
    cv2.imshow('Frame', frame_with_square)

    # Introduce a delay for visibility (adjust the delay as needed)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # 100 ms delay
        break

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()
