import cv2, sys,os, random, string, shutil
from face_detection.exception import FaceDetectionException
from face_detection.logger import logging


class FaceDetectionWebcam:

    def load_camera(self,recorded_video_path):
        try:
            destination_path = os.path.join(os.getcwd(),'static','output')
            shutil.rmtree(destination_path)
            if os.path.exists(destination_path) == False:
                print(destination_path)
                os.makedirs(destination_path)
            file_string = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=4))+'.avi'
            file_path = os.path.join(destination_path,file_string)
            print(file_path)
            # Create a CascadeClassifier Object
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            cap = cv2.VideoCapture(recorded_video_path)

            fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
            
            out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

            while(True):
                ret, frame = cap.read()

                # Convert to grayscale  
                #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(frame, 1.1, 4)

                for (x, y, w, h) in faces:  
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                out.write(frame)

                #cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            
            cap.release()
            out.release()
            cv2.destroyAllWindows()

        except Exception as e:
            raise FaceDetectionException(e,sys)

