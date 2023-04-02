import keyboard


#https://github.com/Camille-Gouneau/Ryuforcement
def keyboard_controller(max_gesture_key):
    comboSequence_Enabled = False
    if keyboard.is_pressed('left') or max_gesture_key=='left':
        action = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('right') or max_gesture_key=='right':
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif keyboard.is_pressed('up')  or max_gesture_key=='jump':
        action = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('down') or max_gesture_key=='crouch':
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('a') or max_gesture_key == "crouchpunch": #crouchpunch
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    # elif keyboard.is_pressed('s'): # lightpunch
    #     action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif keyboard.is_pressed('d') or max_gesture_key == "hardpunch": #hardpunch
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('e') or max_gesture_key == "uppercut": #uppercut
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('w') or max_gesture_key == "highkick": #highkick
        action = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('q') or max_gesture_key == "crouchslide": #crouchslide
        action = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]        
    elif keyboard.is_pressed('space') or max_gesture_key == "hadoken": #hadokoen
        action = [
                [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0], 
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1], 
                [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1], 
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                ]
        comboSequence_Enabled = True
    elif keyboard.is_pressed('p') or max_gesture_key == "backkick": #backkick
        action = [
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], 
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0], 
                [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0], 
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
                [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1], 
                [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0], 
                [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], 
                [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], 
                [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], 
                [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], 
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1], 
                [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0], 
                [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0], 
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0], 
            ]
        comboSequence_Enabled = True
    # elif keyboard.is_pressed('o'): #shoryuken
    #     action = [
    #         [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    #         [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    #         [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
    #         [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    #         [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    #         [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    #         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    #         [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    #         [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    #         [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    #         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    #         [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    #         [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    #         [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    #         [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #         [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    #         [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    #         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    #         [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    #         [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    #         [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    #         [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    #         ]
    #     comboSequence_Enabled = True
    elif keyboard.is_pressed('i') or max_gesture_key == "tatsumaki": #tatsumaki
        action = [
        [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0], 
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], 
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0], 
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1], 
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0], 
        [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1], 
        [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1], 
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0], 
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1], 
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], 
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1], 
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
        [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 
        [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0], 
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1], 
        ]
        comboSequence_Enabled = True

    else:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return action,comboSequence_Enabled
