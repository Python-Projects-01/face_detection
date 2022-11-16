let video = document.querySelector("#video");
let camera_button = document.querySelector("#start-camera");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let detect_btn = document.querySelector("#detect_btn");
let result = document.getElementById('result')
let videoSave = document.getElementById('video2');

let camera_stream = null
let media_recorder = null
let blobs_recorded = []
let streams =[]
let random_string = (Math.random() + 1).toString(36).substring(7);

window.onload = function() {
    document.getElementById('recorded_video_display').style.display = 'none';
    start_button.style.display = 'none'
    stop_button.style.display = 'none'
  };

camera_button.addEventListener("click", async function(){
    camera_stream = await navigator.mediaDevices.getUserMedia({video:true})
    video.srcObject = camera_stream
    camera_button.style.backgroundColor = '#0d6efd';
    start_button.style.display = 'block'
})

function form_handler(event) {
    event.preventDefault();
}

start_button.addEventListener('click', function(){
    start_button.style.backgroundColor = '#0d6efd'
    stop_button.style.display = 'block';
    start_button.style.display = 'none';

    media_recorder = new MediaRecorder(camera_stream, {mimeType:'video/webm'})

    media_recorder.addEventListener('dataavailable', function(e){
        blobs_recorded.push(e.data)
    })

    media_recorder.addEventListener('stop', function(){
        
        var xhr = new XMLHttpRequest();
    
        let video_local = URL.createObjectURL(new Blob(blobs_recorded,{type:'video/webm'}));

        let obj={
            name : Date.now()+"Recording",
            url:video_local
        }
        streams.push(obj)
        
        streams.forEach(stream =>{

            res = `

            <a download="${random_string + "recording.webm"}" href="${stream.url}" id="url_link" onclick="link_button()">Download Video</a>
            `
            $("#result").append(res)
        });
       
        document.getElementById('recorded_video').style.display = 'none'
        videoSave.src = video_local
        document.getElementById('recorded_video_display').style.display = 'block'
        media_recorder=null
        blobs_recorded=[]
    
    })
    media_recorder.start(1000);
})

stop_button.addEventListener('click',function(){
    stop_button.style.backgroundColor = '#0d6efd'
    media_recorder.stop();
    
})
detect_btn.addEventListener('click',function(){
    window.location.href = '/download_video';
})

function link_button(){
    document.querySelector('#url_link').style.color="red";
    var xhr = new XMLHttpRequest();
    var params = `${random_string + "recording.webm"}`
    xhr.open('POST','/webcam'+"?"+"arg2"+"="+params,true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.href = '/download_video';
       }
    };
    xhr.onload = function(){};
    xhr.send()
}


