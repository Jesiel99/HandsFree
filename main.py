import speech_recognition as sr
from pynput.keyboard import Key, Controller
from Sound import Sound
from googletrans import Translator
import json
import time
import re



with open('config.json') as cf:
    config = json.load(cf)
with open('keyboard_keys_translations.json') as cf:
    keyboard_keys = json.load(cf)


def command(input):
    keyboard = Controller()
#
    import pyautogui
    # pyautogui.keyDown('alt')
    # keyboard.press(Key.alt)
    # time.sleep(1)pynput.keyboard
    # pyautogui.press('tab')
    # keyboard.press(Key.tab)
    # time.sleep(1)

    # keyboard.release(Key.tab)
    # time.sleep(1)
    # pyautogui.keyUp('alt')
    # keyboard.release(Key.alt)

    inputs = input.lower().split("\W+")
    print(inputs)
    current_keyboard_keys = keyboard_keys[config["language"].split("-")[0]]
    if inputs[0] in current_keyboard_keys:
        for command in inputs:
            print('pressed')
            if command in current_keyboard_keys:
                keyboard.press(eval(current_keyboard_keys[command]))
            else:
                keyboard.press(command)
        time.sleep(0.9)
        inputs.reverse()
        for command in inputs:
            print('released')
            if command in current_keyboard_keys:
                keyboard.release(eval(current_keyboard_keys[command]))
            else:
                keyboard.release(command)
    else:
        keyboard.type(input)


def listen():

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=config["ambient_noise"]["duration"])
        print('Listening')
        audio = r.listen(source)  # timeout=3, phrase_time_limit=3
    print('Processing')

    try:
        input = r.recognize_google(audio, language=config["language"]) #Control
        print(input)
        command(input)
    except sr.UnknownValueError as e:
        print(e)
        Sound.error()
    listen()

# def setup_language(language):

    # config['+27792955555']
    # translator = Translator()
    # control = translator.translate("control", src='en', dest='pt')
    # if len(config.keyboard_keys) == 0 or config.keyboard_keys == config.en_keyboard_keys and config.language != "en":
    #     config.keyboard_keys = {}
    #     for en_key in config.en_keyboard_keys:
    #         config.keyboard_keys[translator.translate(en_key, src='en', dest='pt').text] = config.en_keyboard_keys[en_key]


r = sr.Recognizer()
# 7 is just my main Microphone index, remove it and try without any input that it should link to your default microphone
mic = sr.Microphone(7, chunk_size=300)  # USB PnP Sound Device: Audio (hw:1,0)
print(mic.list_microphone_names()[7])
listen()
