'''data = request.get_data()
        new_str = data.decode('utf-8')
        d = json.dumps(new_str)
        mydata = ast.literal_eval(d)
        updated = yaml.load(mydata)
        print(type(updated))
        print(updated)
        
        streams.forEach(stream =>{

            res = `
            <form method="POST">
            <input type="text" name="url" id="url" value="${stream.url}">
           
            </form>
            <table>
            <tr>
            <td>${stream.name}</td>
            <td><a download="${Date.now() + "recording.webm"}" href="${stream.url}">Download Video</a></td>
            </tr>
            </table>
            `
            $("#result").append(res)
        });


   
    destination_path = os.path.join(os.getcwd(),'static','videos')
    recorded_video_path = os.path.join(destination_path,download_flag)
    print("is_EXISTS",os.path.exists(recorded_video_path))

        # Reading image as gray scale image
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

.container{
    position: relative;
    justify-content: center;
    align-items: center;
    /* min-height: 100vh; */
    width: 100%;
    height: 100%;
    display: flex;
}
.container .video-wrapper{
    position: relative;
    width: 700px;
    height: 100%;
    border-radius: 5px;
    overflow: hidden;
    border:15px solid rgba(255,255,255,0.24);
    
}
.my-controls{
    display: flex;
    list-style: none;
    justify-content: center;
}
.my-controls li{
    line-height: 27px;
    padding: 2px;
    margin: 0 15px;
    border-radius: 5%;
    text-align: center;
    font-size: 20px;
    border: 3px solid #f42e79;
    cursor: pointer;
    color: #f42e79;
}
body{
    
    background : #222;
}
<div class="container">
        <div class="video-wrapper" id="recorded_video">
            <video id="video"  autoplay></video> 
            <ul class="my-controls">
                <li id="start-camera">Camera ON</li>
                <li id="start-record">Start Recording</li>
                <li id="stop-record">Stop Recording</li>
            </ul>
        </div>
    </div>
            
    
        
        '''


