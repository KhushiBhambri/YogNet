const video = document.getElementById('video-feed');
const startButton = document.getElementById('start-cam-btn');

const constraints = { audio: false, video: true };

function startCamera() {
  navigator.mediaDevices.getUserMedia(constraints)
    .then(stream => {
      video.srcObject = stream;
      video.play();
    })
    .catch(err => {
      console.error('Could not access camera: ', err.message);
    });
}
startButton.addEventListener('click', () => {
  startCamera();
});
