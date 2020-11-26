import speech_recognition as sr

r = sr.Recognizer()

# harvard = sr.AudioFile('untitled.wav')
# with harvard as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     audio = r.record(source)
# print(r.recognize_google(audio))
# the mute muffled the high tones of the horn the gold ring fits only a pierced-ear the old pan was covered with hard fudge what's the log float in the wide river the node on the stalk of wheat grew daily the Heap of fallen leaves was set on fire right fast if you want to finish early his shirt was clean but one button was gone the barrel of beer was a brew of malt and hops tin cans are absent from store shelves

# this is just main Microphone index, remove it and try without any input that it should link to the default microphone
mic = sr.Microphone(10, chunk_size=200) #7
print(mic.list_microphone_names())
with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.4)
    print('Listening')
    audio = r.listen(source) # timeout=3, phrase_time_limit=3

print('Processing')
print(r.recognize_google(audio))

