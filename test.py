'''data = request.get_data()
        new_str = data.decode('utf-8')
        d = json.dumps(new_str)
        mydata = ast.literal_eval(d)
        updated = yaml.load(mydata)
        print(type(updated))
        print(updated)'''


        
                '''# Reading image as gray scale image
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Search the coordinates of the image
                faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )

                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
'''