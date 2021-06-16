#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
import json
from os import path
from pydub import AudioSegment


class Model(object):

    def __init__(self):
        self.r = sr.Recognizer()

    def predict(self, X, feature_name):
        if X[-3:] == 'mp3':
            self.sound = AudioSegment.from_mp3(X)
            self.sound.export('Speech.wav', format='wav')
            X = 'Speech.wav'
        if X[-3:] == 'm4a':
            self.sound = AudioSegment.from_file(X)
            self.sound.export('Speech.wav', format='wav')
            X = 'Speech.wav'
        with sr.AudioFile(X) as source:
            self.audio_data = self.r.record(source)
            self.text = self.r.recognize_google(self.audio_data)
        self.identity = dict()
        self.identity['text'] = self.text
        json_text = json.dumps(self.identity)
        return json_text
