# from flask import Flask, render_template, Response
# import cv2

# app = Flask(__name__)

# cap = cv2.VideoCapture(0)

# def gen_frames():
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, Response


import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)


def video_feed():
    cap = cv2.VideoCapture(0) # 0 for the default camera
    while True:
        ret, frame = cap.read()
        # show the captured video
        cv2.imshow('video_feed', frame)
        # stop capturing the video when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def start():
    cap = cv2.VideoCapture(0) # 0 for the default camera
    while True:
        ret, frame = cap.read()
        # show the captured video
        cv2.imshow('video_feed', frame)
        # stop capturing the video when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/start')
def run():
    start()
    return 'Video Feed Started!'

if __name__ == '__main__':
    app.run(debug=True)
