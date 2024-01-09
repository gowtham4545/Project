import cv2
import mediapipe as mp

mp_holistic=mp.solutions.holistic
mp_drawing=mp.solutions.drawing_utils
height,width,channel=0,0,0

def setDimension(shape):
    global height,width,channel
    h,w,c=shape
    height=h
    width=w
    channel=c

def mediapipe_detection(image,model):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image.flags.writeable=False
    results=model.process(image)
    image.flags.writeable=True
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    return image,results

def draw_landmarks(image,results):
    mp_drawing.draw_landmarks(image,results.face_landmarks,mp_holistic.FACEMESH_CONTOURS)
    mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(image,results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image,results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)

def collectData(results,dots):
    if results.left_hand_landmarks:
        for id,lm in enumerate(results.left_hand_landmarks.landmark):
            dots['lh'].update({str(id):{'x':int(lm.x*width),'y':int(lm.y*height),'z':int(lm.y*width)}})
    else:
        dots['lh']={}
    
    if results.right_hand_landmarks:
        for id,lm in enumerate(results.right_hand_landmarks.landmark):
            dots['rh'].update({str(id):{'x':int(lm.x*width),'y':int(lm.y*height),'z':int(lm.y*width)}})
    else:
        dots['lh']={}

    if results.pose_landmarks:
        for id,lm in enumerate(results.pose_landmarks.landmark):
            dots['pose'].update({str(id):{'x':int(lm.x*width),'y':int(lm.y*height),'z':int(lm.y*width)}})
    else:
        dots['pose']={}

    if results.face_landmarks:
        for id,lm in enumerate(results.face_landmarks.landmark):
            dots['face'].update({str(id):{'x':int(lm.x*width),'y':int(lm.y*height),'z':int(lm.y*width)}})
    else:
        dots['face']={}

def printI(image,text:str,*args,color=(0,0,0),thickness=1):
    cv2.putText(image,text.format(args),(40,40),cv2.FONT_HERSHEY_TRIPLEX,thickness,color,thickness)