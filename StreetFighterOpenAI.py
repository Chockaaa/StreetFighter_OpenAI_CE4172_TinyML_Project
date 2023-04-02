import retro
import time
import serial
import json
from StreetFighterkeyboardmoves import keyboard_controller

import serial, json, time
retro.data.list_games()


env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()



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

            # bank.append(action)
            # if(reward>0):
            #     print("Reward: ",reward, "Action: ", action)
            #     print(bank[-50:])
            #     print()



        
            
env.close()