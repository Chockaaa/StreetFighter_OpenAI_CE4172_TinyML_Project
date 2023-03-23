import retro
import keyboard
import time


retro.data.list_games()


env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()

#https://github.com/Camille-Gouneau/Ryuforcement
def keyboard_controller():
    if keyboard.is_pressed('left'):
        action = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('right'):
        action = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif keyboard.is_pressed('up'):
        action = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('down'):
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif keyboard.is_pressed('a'):
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif keyboard.is_pressed('s'):
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif keyboard.is_pressed('d'):
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('q'):
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
    elif keyboard.is_pressed('w'):
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
    elif keyboard.is_pressed('e'):
        action = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
    elif keyboard.is_pressed('z'):
        action = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
    else:
        action = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return action


done = False
for game in range(1):
    count = 0
    while not done:
        if done:
            obs = env.reset()
            
        
        action = env.action_space.sample()

        #action = keyboard_controller()

        

        obs, reward, done, info = env.step(action)
        if(reward>0):
            print("Reward: ",reward, "Action: ", action)

        
        # Render the game
        env.render()
        time.sleep(0.01)
        
            
env.close()