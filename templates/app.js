let canvas1 = document.querySelector("#canvas1");
let context = canvas1.getContext("2d");
let video1 = document.querySelector("#video1");

if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia){
    navigator.mediaDevices.getUserMedia({video : true}).then(stream =>{
        video1.srcObject = stream;
        video1.play();
    })
}

document.getElementById('pic').addEventListener('click', () => {
    context.drawImage(video1, 0,0,640,480);
})