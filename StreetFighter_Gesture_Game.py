import retro
import time
import serial
import json
import threading
from StreetFighterkeyboardmoves import keyboard_controller

ser = serial.Serial('COM4', 9600)
env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()

max_gesture_key = "normal"
bank = []
done = False

def render_env():
    bank = []
    done = False
    while not done:
        action,comboSequence_Enabled = keyboard_controller(max_gesture_key)

        if comboSequence_Enabled == True:
            for i in range(len(action)):
                obs, reward, done, info = env.step(action[i])
                env.render()
                time.sleep(0.02)

        else:
            obs, reward, done, info = env.step(action)
            env.render()
            time.sleep(0.02)

def get_gesture_data():
    global max_gesture_key
    while not done:
        if ser.in_waiting > 0:
            gesture_data = ser.readline().decode('utf-8').strip()
            gesture_data_json_object = json.loads(gesture_data)
            max_gesture_key = max(gesture_data_json_object, key=gesture_data_json_object.get)

render_thread = threading.Thread(target=render_env)
gesture_thread = threading.Thread(target=get_gesture_data)

render_thread.start()
gesture_thread.start()

render_thread.join()
gesture_thread.join()

env.close()
