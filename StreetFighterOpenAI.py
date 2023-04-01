import retro
import keyboard
import time


retro.data.list_games()


env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()

#https://github.com/Camille-Gouneau/Ryuforcement
def keyboard_controller():
    comboSequence_Enabled = False
    if keyboard.is_pressed('left'):
        action = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('right'):
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif keyboard.is_pressed('up'):
        action = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('down'):
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]


    elif keyboard.is_pressed('a'): #crouchpunch
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    # elif keyboard.is_pressed('s'): # lightpunch
    #     action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif keyboard.is_pressed('d'): #hardpunch
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('e'): #uppercut
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('w'): #highkick
        action = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # elif keyboard.is_pressed('q'): #crouchslide
    #     action = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]        
    elif keyboard.is_pressed('space'): #hadokoen
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
    elif keyboard.is_pressed('p'): #backkick
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
    elif keyboard.is_pressed('i'): #tatsumaki
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


bank = []
done = False
for game in range(1):
    while not done:
        if done:
            obs = env.reset()
        #action,comboSequence_Enabled = env.action_space.sample(),False
        action,comboSequence_Enabled = keyboard_controller()

        if comboSequence_Enabled == True:
            for i in range(len(action)):
                obs, reward, done, info = env.step(action[i])
                env.render()
                time.sleep(0.01)

        else:
            obs, reward, done, info = env.step(action)
            env.render()
            time.sleep(0.01)

            bank.append(action)
            if(reward>0):
                print("Reward: ",reward, "Action: ", action)
                print(bank[-50:])
                print()



        
            
env.close()