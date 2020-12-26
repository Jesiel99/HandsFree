import abc
from abc import ABC, ABCMeta
from voice_recognition.AbstractRecognizer import AbstractRecognizer


class Google(AbstractRecognizer):

    def recognize(self): #audio_data, key=None, language="en-US", show_all=False):
        print('hi')# super.recognizer.recognize_google(audio_data, key=key, language=language, show_all=show_all)