import cv2
import numpy as np

# Path to the video file
video_path = 'Resources/video_2023-12-09_18-13-38.mp4'

# Initialize global variables for the red square
red_square_top_left = None
red_square_size = 200


# Mouse callback function to set the top left corner of the red square
def set_red_square_top_left(event, x, y, flags, param):
    global red_square_top_left
    if event == cv2.EVENT_LBUTTONDOWN:
        red_square_top_left = (x, y)


# Function to find the brightest spot within the red square
def find_brightest_spot_in_square(frame, top_left, size):
    # Define the region of interest (ROI)
    roi = frame[top_left[1]:top_left[1] + size, top_left[0]:top_left[0] + size]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Find the brightest spot in the ROI
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray_roi)
    maxLocGlobal = (maxLoc[0] + top_left[0], maxLoc[1] + top_left[1])
    return maxLocGlobal


# Function to draw a red square
def draw_red_square(frame, top_left, size):
    if top_left is not None:
        bottom_right = (top_left[0] + size, top_left[1] + size)
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
    return frame


# Function to draw a green square around the brightest spot
def draw_green_square(frame, center, size=20):
    top_left = (max(center[0] - size, 0), max(center[1] - size, 0))
    bottom_right = (min(center[0] + size, frame.shape[1]), min(center[1] + size, frame.shape[0]))
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
    return frame


# Open the video
cap = cv2.VideoCapture(video_path)
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Frame", set_red_square_top_left)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Draw the red square if it's set
    frame = draw_red_square(frame, red_square_top_left, red_square_size)

    # Find and draw the brightest spot if the red square is set
    if red_square_top_left is not None:
        brightest_spot = find_brightest_spot_in_square(frame, red_square_top_left, red_square_size)
        frame = draw_green_square(frame, brightest_spot)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Introduce a delay for visibility
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()
