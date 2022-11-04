import cv2, sys
from face_detection.exception import FaceDetectionException
from face_detection.logger import logging

class FaceDetectionWebcam:

    def load_camera(self,video):
        try:
            print(video)
            # Create a CascadeClassifier Object
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            # video_capture = cv2.VideoCapture(0)
            video_capture = cv2.VideoCapture(video)

            while True:
                # Capture frame-by-frame
                ret, frame = video_capture.read()

                # Display the resulting frame
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # When everything is done, release the capture
            video_capture.release()
            cv2.destroyAllWindows()

        except Exception as e:
            raise FaceDetectionException(e,sys)

