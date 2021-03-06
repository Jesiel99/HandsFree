# sudo apt-get install python3-tk python3-dev
# sudo apt install python3-pyaudio
from collections import OrderedDict
import speech_recognition as sr
# from pynput.keyboard import Key, Controller
from Sound import Sound
import pyaudio
# from googletrans import Translator
import json
import time
import re
import pyautogui

pyautogui.PAUSE = 0

with open('config/config.json') as cf:
    config = json.load(cf)
with open('config/command_keys_translations.json') as cf:
    keyboard_command_keys = json.load(cf)
with open('config/special_characters_commands_by_language.json') as spc:
    special_characters_commands_by_language = json.load(spc)
    special_characters_commands = special_characters_commands_by_language[config["language"].split("-")[0]]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
release_after = []
current_keyboard_command_keys = keyboard_command_keys[config["language"].split("-")[0]]
keyboard_symbols_keys = alphabet + numbers
key_voice_commands =  list(current_keyboard_command_keys.keys()) + keyboard_symbols_keys


def press(inputs):
    for voice_key in inputs:
        if voice_key in current_keyboard_command_keys:
            print('pressed: ' + current_keyboard_command_keys[voice_key])
            if current_keyboard_command_keys[voice_key] in ['ctrl', 'shift', 'alt']:
                pyautogui.keyDown(current_keyboard_command_keys[voice_key])
                release_after.append(current_keyboard_command_keys[voice_key])
            else:
                print('released: ' + current_keyboard_command_keys[voice_key])
                pyautogui.press(current_keyboard_command_keys[voice_key])

        else:
            print('pressed: ' + voice_key)
            pyautogui.press(voice_key)
    release_after.reverse()
    time.sleep(1)
    for key in release_after:
        print('released after')
        pyautogui.keyUp(key)


def command(input):
    print(input)
    raw_input = input
    input = ' ' + input.replace('-', ' ').lower() + ' '
    dictionary = {}
    input2 = input
    for element in key_voice_commands:
        while True:
            if len(element) == 1:
                element2 = ' ' + element + ' '
            else:
                element2 = element
            key_index = re.search(r'(' + element2 + ')', input2)
            if key_index is not None:
                dictionary[key_index.start()] = element
                print(key_index.start())
                input2 = input2.replace(element, ' ' * len(element), 1)
            else:
                break
    print(dictionary)
    keyboard_command_inputs = list(OrderedDict(sorted(dictionary.items())).values())
    # elif all(elem in key_voice_commands for elem in inputs):
    print(keyboard_command_inputs)
    # if the input contains just keyboard commands
    if input2.strip() == '':
        press(keyboard_command_inputs)
    elif input.lower() in special_characters_commands:
        pyautogui.press(special_characters_commands[input.lower()])
    else:
        pyautogui.write(raw_input)


def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=config["ambient_noise"]["duration"])
        print('Listening')
        audio = r.listen(source)  # timeout=3, phrase_time_limit=3
    print('Processing')
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
mic = sr.Microphone(6, chunk_size=1000)  # USB PnP Sound Device: Audio (hw:1,0)
print(mic.list_microphone_names()[6])
listen()
# page downdeleteandain'tautistaaldhabiAltarCloudoutside
