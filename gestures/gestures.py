from .positions import *
face,pose,left,right='face','pose','lh','rh'

@handler
def iLoveYou(dots):
    if (bool(dots['lh']) and left_thumb_open(dots) and left_fore_finger_up(dots) and left_middle_finger_down(dots) and left_ring_finger_down(dots) and left_small_finger_up(dots)) or (bool(dots['rh']) and right_thumb_open(dots) and right_fore_finger_up(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_up(dots)):
        return True
    return False

@handler
def father(dots):
    return openRightFist(dots) and dots[face]['151']['x']==dots[right]['4']['x']

@handler
def mother(dots):
    if openRightFist(dots) and intersect(dots,right,4,face,152):
        return True
    return False

@handler
def house(dots):
    if openLeftFist(dots) and openRightFist(dots) and intersect(dots,left,12,right,12) and abs(dots[right]['0']['x']-dots[left]['0']['x'])>80 and abs(dots[left]['7']['x']-dots[left]['15']['x'])<=10 and abs(dots[right]['7']['x']-dots[right]['15']['x'])<=10:
        return True
    
@handler
def hello(dots):
    return openRightFist(dots) and intersect(dots,face,70,right,8)

@handler
def thanks(dots):
    return openLeftFist(dots) and openRightFist(dots) and intersect(dots,left,12,right,12) and intersect(dots,left,12,face,13) and abs(dots[left]['4']['x']-dots[right]['4']['x'])>80 

