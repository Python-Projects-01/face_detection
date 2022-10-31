
<h1 align="center">Python Face Detection App </h1>

Application url : [URL_Shortner](https://ineuronurl.herokuapp.com/)

<h5> This Application will detect object of interest (human face) in real time. Application will detect face either from user uploaded image or frames from web camera. </h5>

## <img src="https://c.tenor.com/NCRHhqkXrJYAAAAi/programmers-go-internet.gif" width="25">  <b>Approach</b>

- Use Opencv
- Run web server with Flask

## <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="25"> <b> API</b>

1. Project Flowchart

![Screenshot](snippets/face_authenticator.png)
2. Landing page of application

![Screenshot](snippets/snippet1.png)

3. option to upload image

![Screenshot](snippets/snippet5.png)

4. Display uploaded image in frame

![Screenshot](snippets/snippet2.png)

5. Display face detected of uploaded image

![Screenshot](snippets/snippet3.png)

6. Display face detected using webcam

![Screenshot](snippets/snippet4.png)

 ## 💻 How to setup:



Creating conda environment
```
conda create -p venv python==3.8 -y
```

activate conda environment
```
conda activate ./venv
```

Install requirements
```
pip install -r requirements.txt
```
Run the live server using flask
```
python app.py
```
To launch flask ui
```
http://localhost:5000/
```

 ## <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width ="25"><b> Technologies Used</b>


 <p align="center">

 1. Opencv
 2. Flask

 ## 🏭 Industrial Use-cases 

- Recognizing Drivers in Cars
- Attendance System
- Identifying accounts on social media
 
 ## 👋 Conclusion

  We have shown the way to implement face detection using image upload and webcam. 