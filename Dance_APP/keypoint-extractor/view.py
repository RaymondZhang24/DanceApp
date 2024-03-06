import cv2
import json

# Load keypoints from JSON file
with open('test1.json', 'r') as f:
    keypoints_dict = json.load(f)

# Path to the original video
video_path = 'videos/a.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create video writer object
output_video = cv2.VideoWriter('output/video_with_keypoints.avi',
                                cv2.VideoWriter_fourcc(*'XVID'),
                                fps,
                                (frame_width, frame_height))

# Iterate through each frame
frame_number = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Overlay keypoints on the frame
    keypoints = keypoints_dict[frame_number]
    for keypoint in keypoints.values():
        x, y, _ = keypoint
        cv2.circle(frame, (int(x * frame_width), int(y * frame_height)), 5, (0, 255, 0), -1)

    # Write the frame with keypoints to the output video
    output_video.write(frame)

    # Display the frame
    cv2.imshow('Video with Keypoints', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    frame_number += 1

# Release video capture and writer objects
cap.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
