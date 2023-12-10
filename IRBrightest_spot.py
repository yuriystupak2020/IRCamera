import cv2
import numpy as np

# Path to the uploaded video file
video_path = 'Resources/video_2023-12-09_18-13-38.mp4'


# Function to find the brightest spot in the frame
def find_brightest_spot(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the coordinates of the maximum value (brightest spot)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    return maxLoc


# Function to draw a green square around the brightest spot
def draw_green_square(frame, center, size=20):
    # Calculate the coordinates of the top-left and bottom-right corners
    top_left = (max(center[0] - size, 0), max(center[1] - size, 0))
    bottom_right = (min(center[0] + size, frame.shape[1]), min(center[1] + size, frame.shape[0]))

    # Draw a green square
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    return frame


# Open the video
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")

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

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()
