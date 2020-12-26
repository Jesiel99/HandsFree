import abc
from abc import ABC, ABCMeta
import speech_recognition as sr


class AbstractRecognizer(metaclass=abc.ABCMeta):

    # @property
    # def
    @abc.abstractmethod
    def recognize(self):
        raise NotImplementedError

class Asda:

    def __init__(self):
        print('init')
