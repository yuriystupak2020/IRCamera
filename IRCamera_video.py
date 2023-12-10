import cv2
import numpy as np

# Function to process each frame
def process_frame(frame, threshold_value):
    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply threshold
    _, thresholded_frame = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY)

    # Optionally, find and process contours here

    return thresholded_frame

# Path to the downloaded video file
video_path = 'Resources/video_2023-12-09_14-17-39.mp4'

# Open a video capture object for the video file
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Set a threshold value
threshold_value = 127  # Adjust this value based on your requirements

# Calculate the delay between frames (in ms)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        break

    # Process the frame
    processed_frame = process_frame(frame, threshold_value)

    # Display the processed frame
    cv2.imshow('Infrared Spot Detection', processed_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
