import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    # frame is a NumPy array, It represents the first image that video captures
    # check is a bool data type , it return true if Python is able to read VideoCapture object
    check, frame = video.read()
    # Convert each frame into a gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Convert gray scale frame to GaussianBlur
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    # store the first frame of video
    if first_frame is None:
        first_frame = gray
        continue
    
    # Calculate difference between first frame and other frames 
    delta_frame = cv2.absdiff(first_frame, gray)

    # provide a threshold value such that it willl convert difference less than 30 to black 
    # If threshold value is greater than 30 will turn it into white color
    thresh_delta = cv2.threshold(delta_frame,30, 255, cv2.THRESH_BINARY)[1]

    thresh_delta = cv2.dilate(thresh_delta,None, iterations=0)

    # Define contours , basically defining borders
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Removes nosies and shadows
    for contour in cnts:
        # It will keep only that part which is greater than 1000 pixels
        if cv2.contourArea(contour) < 1000:
            continue
        # Creates a rectangular box around the object in frame
        (x, y ,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)



    cv2.imshow("Capture", frame)
    cv2.imshow("Capturing", gray)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("thresh", thresh_delta)

    # This will generate a new frame after every 1 ms
    key = cv2.waitKey(1)

    # Once user enters 'q' the window will be detroyed
    if key == ord('q'):
        break

    # Wait until user presses key
    cv2.waitKey(0)

    # closes the window based on waitkey parameter 
    cv2.destroyAllWindows()
