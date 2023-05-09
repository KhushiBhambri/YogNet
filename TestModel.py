import cv2
import numpy as np
import tensorflow as tf

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
