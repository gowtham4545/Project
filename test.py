import cv2
import mediapipe as mp
import time

# Creating a screen object
cap=cv2.VideoCapture(0)

# Creating a hand tracking and detecting model
mpHands=mp.solutions.hands
hands=mpHands.Hands()

# Module that contains methods place edges on the patterns
mpDraw=mp.solutions.drawing_utils

dots={}
# Loop that runs the camera (for every millisec)
while True:
    # Taking the camera input
    success,img=cap.read()

    # Converting into RGB image object
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # The output processed by the model
    results=hands.process(imgRGB)

    # Prints detect hand landmarks, (i.e. positions on the screen)
    '''
    print(results.multi_hand_landmarks)
    '''

    height,width,channel=img.shape


    x='x';y='y'
    # Assigning dots and edges for the patterns
    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id,lm in enumerate(handLMS.landmark):
                # Printing id's of the dots/landmarks
                dots.update({str(id):{x:int(lm.x*width),y:int(lm.y*height)}})
                cv2.putText(img,str(id),(int(lm.x*width)+20,int(lm.y*height)),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
            mpDraw.draw_landmarks(img,handLMS,mpHands.HAND_CONNECTIONS)

        if dots['8'][y]<dots['5'][y] and dots['12'][y]>dots['9'][y] and dots['16'][y]>dots['13'][y] and dots['20'][y]>dots['17'][y] and abs(dots['4'][x]-dots['2'][x])<50:
            cv2.putText(img,'One',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        elif dots['8'][y]<dots['5'][y] and dots['12'][y]<dots['9'][y] and dots['16'][y]>dots['13'][y] and dots['20'][y]>dots['17'][y] and abs(dots['4'][x]-dots['2'][x])<50:
            cv2.putText(img,'Two',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        elif dots['8'][y]<dots['5'][y] and dots['12'][y]<dots['9'][y] and dots['16'][y]<dots['13'][y] and dots['20'][y]>dots['17'][y] and abs(dots['4'][x]-dots['2'][x])<50:
            cv2.putText(img,'Three',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        elif dots['8'][y]<dots['5'][y] and dots['12'][y]<dots['9'][y] and dots['16'][y]<dots['13'][y] and dots['20'][y]<dots['17'][y] and abs(dots['4'][x]-dots['2'][x])<50:
            cv2.putText(img,'Four',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        elif dots['8'][y]<dots['5'][y] and dots['12'][y]<dots['9'][y] and dots['16'][y]<dots['13'][y] and dots['20'][y]<dots['17'][y] and abs(dots['4'][x]-dots['2'][x])>50:
            cv2.putText(img,'Five',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        else:
            cv2.putText(img,'Hello',(40,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

    # Displaying the input
    cv2.imshow("Test Display",img)
    cv2.waitKey(1)

print(dots['1'])