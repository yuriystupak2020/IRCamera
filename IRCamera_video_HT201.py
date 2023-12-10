import cv2
import numpy as np


# Callback function to draw a green square around the click position
def draw_square(event, x, y, flags, param):
    global top_left_corner, bottom_right_corner, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = (max(x - 25, 0), max(y - 25, 0))
        bottom_right_corner = (min(x + 25, frame.shape[1]), min(y + 25, frame.shape[0]))


# Initialize the top-left and bottom-right corners of the square
top_left_corner = None
bottom_right_corner = None

# Capture video
#cap = cv2.VideoCapture(0)  # Change the argument if you're using a video file

# Path to the downloaded video file
video_path = 'Resources/video_2023-12-09_14-17-39.mp4'

# Open a video capture object for the video file
cap = cv2.VideoCapture(video_path)


cv2.namedWindow("Video")
cv2.setMouseCallback("Video", draw_square)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # If the square exists, draw it and find the brightest spot
    if top_left_corner and bottom_right_corner:
        cv2.rectangle(frame, top_left_corner, bottom_right_corner, (0, 255, 0), 2)

        # Crop to the square area
        square_area = frame[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]]

        # Convert to grayscale and find the brightest spot
        gray_area = cv2.cvtColor(square_area, cv2.COLOR_BGR2GRAY)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray_area)
        cv2.circle(square_area, maxLoc, 5, (255, 0, 0), -1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
