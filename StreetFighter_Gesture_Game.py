import retro
import time
import serial
import json
import threading
from StreetFighterkeyboardmoves import keyboard_controller
from queue import Queue

ser = serial.Serial('COM4', 9600)
env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
obs = env.reset()

max_gesture_key = "normal"
gesture_queue = Queue()
gesture_queue.put(max_gesture_key)

bank = []
done = False

def render_env():
    global max_gesture_key
    global gesture_queue
    bank = []
    done = False
    while not done:
        action, comboSequence_Enabled = keyboard_controller(gesture_queue.get())

        if comboSequence_Enabled == True:
            for i in range(len(action)):
                obs, reward, done, info = env.step(action[i])
                env.render()
                time.sleep(0.01)

                if not gesture_queue.empty():  # if the queue is not empty, pop the next gesture
                    gesture_queue.get()

            max_gesture_key = "normal"
        else:
            obs, reward, done, info = env.step(action)
            env.render()
            time.sleep(0.01)

        if gesture_queue.empty():  # if the queue is empty, add "normal"
            gesture_queue.put("normal")

def get_gesture_data():
    global max_gesture_key
    global gesture_queue
    while not done:
        if ser.in_waiting > 0:
            gesture_data = ser.readline().decode('utf-8').strip()
            gesture_data_json_object = json.loads(gesture_data)
            max_gesture_key = max(gesture_data_json_object, key=gesture_data_json_object.get)
            print(max_gesture_key)
            gesture_queue.put(max_gesture_key)

render_thread = threading.Thread(target=render_env)
gesture_thread = threading.Thread(target=get_gesture_data)

render_thread.start()
gesture_thread.start()

render_thread.join()
gesture_thread.join()

env.close()