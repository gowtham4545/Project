import cv2
import mediapipe as mp

mpPose=mp.solutions.pose
pose=mpPose.Pose()

cap=cv2.VideoCapture(0)


while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    print(results.pose_landmarks)
    cv2.imshow('Image',img)
    cv2.waitKey(1)