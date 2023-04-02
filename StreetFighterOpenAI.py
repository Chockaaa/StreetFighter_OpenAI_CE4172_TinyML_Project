import retro
import time
import serial
import json
from StreetFighterkeyboardmoves import keyboard_controller
#retro.data.list_games()


ser = serial.Serial('COM4', 9600)

env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()


max_gesture_key = "normal"
bank = []
done = False
for game in range(1):
    while not done:
        if ser.in_waiting > 0:
            gesture_data = ser.readline().decode('utf-8').strip()
            gesture_data_json_object = json.loads(gesture_data)
            max_gesture_key = max(gesture_data_json_object, key=gesture_data_json_object.get)
            print(gesture_data_json_object)
            print(max_gesture_key)
        
        if done:
            obs = env.reset()
        #action,comboSequence_Enabled = env.action_space.sample(),False
        action,comboSequence_Enabled = keyboard_controller(max_gesture_key)

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

        max_gesture_key = "normal"
env.close()