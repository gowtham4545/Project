from gestures import gestures as gstr
from gestures.init import *
from threading import Thread
import cv2
from colorama import Fore, Style
from modules import speech

def daemon():
    print(Fore.GREEN + "Daemon Capturing ...")
    buffer = ['']
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
                if gesture != buffer[-1]:
                    buffer.append(gesture)
                break
        printI(image, gesture)
        draw_landmarks(image, results)
        cv2.imshow("Sign2Sound", image)
        key = cv2.waitKey(10)

        if key & 0xFF == ord('q'):
            print(Fore.RED + 'Daemon Terminating ...')
            print(Fore.MAGENTA+'Click Enter to exit:')
            exit(0)

        if key & 0xFF == ord('p'):
            print(Fore.CYAN + str(buffer))

        if key & 0xFF == ord('s'):
            speak=Thread(target=speech(buffer),daemon=True,args=())
            speak.start()


if __name__ == "__main__":
    holistic = mp_holistic.Holistic()

    background = Thread(target=daemon, daemon=True, args=())

    background.start()

    input()
    print(Style.RESET_ALL+"Exiting ...")
