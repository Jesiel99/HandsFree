#sudo apt-get install python3-tk python3-dev
#sudo apt install python3-pyaudio
import speech_recognition as sr
# from pynput.keyboard import Key, Controller
from Sound import Sound
import pyaudio
# from googletrans import Translator
import json
import time
import re
import pyautogui


with open('config/config.json') as cf:
    config = json.load(cf)
with open('config/command_keys_translations.json') as cf:
    keyboard_command_keys = json.load(cf)
with open('config/special_characters_commands_by_language.json') as spc:
    special_characters_commands_by_language = json.load(spc)
    special_characters_commands = special_characters_commands_by_language[config["language"].split("-")[0]]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def command(input):
    inputs = re.split(" |-", input.lower())
    print(input)
    print(inputs)
    release_after = []
    current_keyboard_command_keys = keyboard_command_keys[config["language"].split("-")[0]]
    keyboard_symbols_keys = alphabet + numbers
    key_voice_commands = keyboard_symbols_keys + list(current_keyboard_command_keys.keys())
    if all(elem in key_voice_commands for elem in inputs):
        for index, voice_key in inputs:
            print('pressed')
            if voice_key in current_keyboard_command_keys:
                pyautogui.keyDown(current_keyboard_command_keys[voice_key])
                if current_keyboard_command_keys[voice_key] in ['ctrl', 'shift', 'alt']:
                    release_after.append(current_keyboard_command_keys[voice_key])
                else:
                    pyautogui.keyUp(current_keyboard_command_keys[voice_key])
            else:
                pyautogui.press(voice_key)
        release_after.reverse()
        for key in release_after:
            print('released after')
            pyautogui.keyUp(key)
    elif input.lower() in special_characters_commands:
        pyautogui.press(special_characters_commands[input.lower()])
    else:
        pyautogui.write(input)

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=config["ambient_noise"]["duration"])
        print('Listening')
        audio = r.listen(source)  # timeout=3, phrase_time_limit=3
    print('Processing')
#no venha mais ningum ta mim
    try:
        input = r.recognize_google(audio, language=config["language"])
        print(input)
        command(input)
    except sr.UnknownValueError as e:
        print(e)
        # Sound.error()
    listen()

r = sr.Recognizer()
# 7 is just my main Microphone index, remove it and try without any input that it should link to your default microphone
mic = sr.Microphone(6, chunk_size=300)  # USB PnP Sound Device: Audio (hw:1,0)
print(mic.list_microphone_names()[6])
listen()
