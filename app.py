from gestures import gestures as gstr
from gestures.init import *
from threading import Thread, Event
import cv2


buffer = []
holistic = mp_holistic.Holistic()
key=int(0)


def daemon():
    capture = cv2.VideoCapture(0)
    capture.set(3, 1280)
    capture.set(4, 700)
    dots = {'face': {}, 'lh': {}, 'rh': {}, 'pose': {}}
    while capture.isOpened():
        ret, frame = capture.read()
        image, results = mediapipe_detection(frame, holistic)
        width, height, channel = image.shape
        collectData(results, dots, width, height)
        gesture = ''
        for name in gstr.__all__:
            func = getattr(gstr, name)
            if func(dots):
                gesture = name
                break
        printI(image,gesture)
        draw_landmarks(image, results)
        cv2.imshow("Sign2Sound", image)
        k = cv2.waitKey(10)
        key=k

def interface():
    while True:
        if key  & 0xFF=='q':
            return
        elif key & 0xFF=='p':
            print(buffer)

background = Thread(target=daemon, daemon=True, args=())
background.start()

user=Thread(daemon=True,target=interface)
interface()
user.start()
input()
print(buffer)