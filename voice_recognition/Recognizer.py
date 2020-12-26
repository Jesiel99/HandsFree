import abc
from abc import ABC, ABCMeta
import speech_recognition as sr
# import AbstractRecognizer
from voice_recognition.AbstractRecognizer import AbstractRecognizer


class Recognizer:

    def __new__(cls, class_name: str):
        cls.recognizer = sr.Recognizer()
        subs = AbstractRecognizer.__subclasses__()
        print(cls.__name__)
        for sub in subs:
            # print(sub.__name__.lower() + ' = ')
            if cls != sub and sub.__name__.lower() == class_name.lower():
                return sub()
        else:
            raise ModuleNotFoundError

