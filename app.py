from gestures import gestures as gstr
from gestures.init import *
from threading import Thread, Event
import cv2


buffer = []
holistic = mp_holistic.Holistic()


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
        print(dots)
        gesture = ''
        for name in gstr.__all__:
            func = getattr(gstr, name)
            if func(dots):
                # buffer.append(name)
                gesture = name
                break
        printI(image,gesture)
        draw_landmarks(image, results)
        cv2.imshow("Sign2Sound", image)
        key = cv2.waitKey(10)


background = Thread(target=daemon, daemon=True, args=())
background.start()
input('Press Enter to Exit:')
