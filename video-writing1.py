'''
The program is written to write/save a video from webcamera
'''
import cv2

#output video configuration
video_writing_filepath = 'webcam.avi'
frame_width = 600
frame_height = 600
frame_rate = 30

#defining codec
video_obj = cv2.VideoWriter_fourcc(*'MJPG')
video_output = cv2.VideoWriter(video_writing_filepath,video_obj,frame_rate,(frame_width,frame_height))

#Access the default web camera
capture = cv2.VideoCapture(0)

if capture.isOpened():
    print('Video recording started. Press q to stop recording')
    while True:
        ret,frame = capture.read()
        if not ret:
            print('Failed to read from camera')
            break
        #resizing the video frame
        frame_resize = cv2.resize(frame,(frame_width,frame_height))
        #Saving the recorded video to file
        video_output.write(frame_resize)
        #Showing the frame
        cv2.imshow(f'{video_writing_filepath}',frame_resize)
        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    video_output.release()
    cv2.destroyAllWindows()
    print(f'Video recording stopped and saved to file {video_writing_filepath}')
else:
    print('Web camera not available')

