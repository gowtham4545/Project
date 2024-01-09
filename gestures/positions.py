def handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except:
            return False
    return wrapper

@handler
def left_thumb_open(dots):
    if abs(dots['lh']['3']['x']-dots['lh']['5']['x'])>30:
        return True

@handler
def left_thumb_closed(dots):
    if abs(dots['lh']['3']['x']-dots['lh']['5']['x'])<30:
        return True

@handler
def left_fore_finger_up(dots):
    if dots['lh']['8']['y']<dots['lh']['5']['y']:
        return True

@handler
def left_fore_finger_down(dots):
    if dots['lh']['8']['y']>dots['lh']['5']['y']:
        return True

@handler
def left_middle_finger_up(dots):
    if dots['lh']['12']['y']<dots['lh']['9']['y']:
        return True

@handler
def left_middle_finger_down(dots):
    if dots['lh']['12']['y']>dots['lh']['9']['y']:
        return True

@handler
def left_ring_finger_up(dots):
    if dots['lh']['16']['y']<dots['lh']['13']['y']:
        return True

@handler
def left_ring_finger_down(dots):
    if dots['lh']['16']['y']>dots['lh']['13']['y']:
        return True

@handler
def left_small_finger_up(dots):
    if dots['lh']['20']['y']<dots['lh']['17']['y']:
        return True

@handler
def left_small_finger_down(dots):
    if dots['lh']['20']['y']>dots['lh']['17']['y']:
        return True

@handler
def left_thumb_up(dots):
    if abs(dots['lh']['3']['y']-dots['lh']['5']['y'])>30:
        return True

@handler
def left_thumb_down(dots):
    if abs(dots['lh']['3']['y']-dots['lh']['5']['y'])<30:
        return True
    
@handler
def right_thumb_open(dots):
    if abs(dots['rh']['3']['x']-dots['rh']['5']['x'])>30:
        return True

@handler
def right_thumb_closed(dots):
    if abs(dots['rh']['3']['x']-dots['rh']['5']['x'])<30:
        return True

@handler
def right_fore_finger_up(dots):
    if dots['rh']['8']['y']<dots['rh']['5']['y']:
        return True

@handler
def right_fore_finger_down(dots):
    if dots['rh']['8']['y']>dots['rh']['5']['y']:
        return True

@handler
def right_middle_finger_up(dots):
    if dots['rh']['12']['y']<dots['rh']['9']['y']:
        return True
    
@handler
def right_middle_finger_down(dots):
    if dots['rh']['12']['y']>dots['rh']['9']['y']:
        return True

@handler
def right_ring_finger_up(dots):
    if dots['rh']['16']['y']<dots['rh']['13']['y']:
        return True

@handler
def right_ring_finger_down(dots):
    if dots['rh']['16']['y']>dots['rh']['13']['y']:
        return True

@handler
def right_small_finger_up(dots):
    if dots['rh']['20']['y']<dots['rh']['17']['y']:
        return True

@handler
def right_small_finger_down(dots):
    if dots['rh']['20']['y']>dots['rh']['17']['y']:
        return True

@handler
def right_thumb_up(dots):
    if abs(dots['rh']['3']['y']-dots['rh']['5']['y'])>30:
        return True

@handler
def right_thumb_down(dots):
    if abs(dots['rh']['3']['y']-dots['rh']['5']['y'])<30:
        return True

@handler
def openLeftFist(dots):
    if(bool(dots['lh']) and left_fore_finger_up(dots) and left_middle_finger_up(dots) and left_ring_finger_up(dots) and left_small_finger_up(dots)):
        return True
    return False

@handler
def openRightFist(dots):
    if(bool(dots['rh']) and right_fore_finger_up(dots) and right_middle_finger_up(dots) and right_ring_finger_up(dots) and right_small_finger_up(dots)):
        return True
    return False

@handler
def intersect(dots,g1,p1,g2,p2):
    return abs(dots[g1][str(p1)]['x']-dots[g2][str(p2)]['x'])<20 and abs(dots[g1][str(p1)]['y']-dots[g2][str(p2)]['y'])<20

