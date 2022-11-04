import cv2, os, sys, shutil
from face_detection.exception import FaceDetectionException
from face_detection.logger import logging

class FaceDetectionImage:
    def __init__(self,image_path ):
        self.image_path = image_path

    
    def display_image(self) :
        try:
            
            # Create a CascadeClassifier Object
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            # Black and White image (2 channels)
            img = cv2.imread(self.image_path)

            # Will print shape of numpy array ie(426,500)
            resized_img = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))

            # Reading image as gray scale image
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Search the coordinates of the image
            faces = face_cascade.detectMultiScale(gray_img , scaleFactor = 1.05, minNeighbors =5)


            for x,y,w,h in faces:
                img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)


            # Opens a window to show image
            # Here People is name of window
            #cv2.imshow("People", img)
            saved_file_path = os.path.join(os.getcwd(),'uploads\\images\\')

            absolute_path =os.path.abspath(saved_file_path)
           

            if os.path.exists(absolute_path):
                shutil.rmtree(absolute_path)

            destination_path = os.makedirs(absolute_path)

            filename = 'savedImage.jpg'

            cv2.imwrite(filename, img)

            source_path = os.path.join(os.getcwd())

            

            
        except Exception as e:
            sharing = FaceDetectionException(e,sys)
            logging.info(sharing.error_message)

