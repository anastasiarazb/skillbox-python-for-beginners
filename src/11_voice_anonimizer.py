import speech_recognition as sr
import playsound
import gtts
import os


def user_input():

    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        audio = voice_recognizer.listen(source)

    voice_text = voice_recognizer.recognize_google(audio, language='ru')
    return voice_text

def reply(text):
    voice = gtts.gTTS(text, lang='ru')
    audio_file = 'audio.mp3'
    voice.save(audio_file)

    playsound.playsound(audio_file)
    os.remove('audio.mp3')


user_text = user_input()
reply(user_text)