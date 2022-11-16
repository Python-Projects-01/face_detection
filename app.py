import sys, os,shutil, time
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import (
    Flask,
    send_file,
    abort,
    render_template,
    request,
    url_for,
    flash,
    redirect,
)
from face_detection.logger import logging
from face_detection.exception import FaceDetectionException
from face_detection.components.face_detect_image import FaceDetectionImage
from face_detection.components.face_detect_webcam import FaceDetectionWebcam
from ast import literal_eval
from urllib import request as req


from flask import send_from_directory

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, "uploads")
download_flag = None

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        sharing = FaceDetectionException(e, sys)
        logging.info(sharing.error_message)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/image", methods=["GET", "POST"])
def upload_file():
    
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file present")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            print("No file selected")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # print(file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("download_file", name=filename))
    return render_template("image.html")



@app.route("/uploads/<name>")
def download_file(name):
    img_path = os.path.join(UPLOAD_FOLDER, name)
    face_detect_obj = FaceDetectionImage(image_path=img_path)
    face_detect_obj.display_image()
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route("/webcam", methods=["GET", "POST"])
def webcam():
    try:
        if request.method == 'POST':
            print("webcam Hitted")
            query_param_recieved = request.args
            query_param_dict = query_param_recieved.to_dict()
            #received_video_link = query_param_dict.get("arg1")
            global download_flag
            download_flag = query_param_dict.get("arg2")
            path_to_download_folder = str(os.path.join(Path.home(), "Downloads",download_flag))
            isExist_downloads_path = os.path.exists(path_to_download_folder)
            downloads=os.path.join('~\Downloads',download_flag)
            path_to_download  = Path(os.path.expanduser(downloads))
            print(path_to_download)
            print(os.path.exists(path_to_download))

            #print("isExist_downloads_path",downloads)
            #print("path_to_download_folder",path_to_download_folder)
            
            #print("isExist_downloads_path",isExist_downloads_path)
            if(download_flag is not None) & (isExist_downloads_path):
                #downloads=os.path.join('~/Downloads',download_flag)
                #downloads_path = os.path.expanduser(downloads)
                if isExist_downloads_path:
                    destination_path = os.path.join(os.getcwd(),'static','videos')
                    shutil.rmtree(destination_path)
                    if os.path.exists(destination_path) == False:
                        os.makedirs(destination_path)
                '''print(path_to_download_folder)
                print(destination_path)'''
            shutil.move(path_to_download_folder,destination_path)

            face_detection = FaceDetectionWebcam()
            recorded_video_path = os.path.join(destination_path,download_flag)
            face_detection.load_camera(recorded_video_path)

        return render_template("webcam.html")

    except Exception as e:
        raise FaceDetectionException(e, sys)

@app.route("/download_video", methods=["GET", "POST"])
def download_video():
    print("download Hitted")
    destination_path = os.path.join(os.getcwd(),'static','output')
    list_of_files =os.listdir(destination_path)
    if len(list_of_files)>=1:
        output_file = list_of_files[0]
        print(output_file)

    updated_video_path = os.path.join(os.getcwd(),'static','output',output_file)
    print(updated_video_path)


    '''output_path = os.path.join(os.getcwd(),'output.avi')
    if os.path.exists(output_path):
        destination_path = os.path.join(os.getcwd(),'static','output')
        if os.path.exists(destination_path) == False:
            print(destination_path)
            os.makedirs(destination_path)
        file_path = os.path.join(destination_path,'output.avi')
        print("file_path",file_path)
        if os.path.exists(file_path):
            os.unlink(file_path)
        time.sleep(3)
        shutil.move(output_path,destination_path)'''
    return render_template("download_video.html",output_file=output_file)

@app.route("/result")
def result():
    destination_path = os.path.join(os.getcwd(),'static','output')
    list_of_files =os.listdir(destination_path)
    if len(list_of_files)>=1:
        output_file = list_of_files[0]
    file_name = 'output/'+output_file
    return render_template("result_image.html",file=file_name)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
