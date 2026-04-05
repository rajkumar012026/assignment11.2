import cv2

video_path = 'webcam.avi'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video source at {video_path}")
    exit()


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video/saved_output.avi', fourcc, fps, (frame_width, frame_height))

print("Reading and saving video... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Write the frame to the output file
    out.write(frame)
    
    cv2.imshow('Video Frame', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 4. Release both objects
cap.release()
out.release()
cv2.destroyAllWindows()
