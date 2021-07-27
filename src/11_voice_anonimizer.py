import playsound
import gtts
import os
import speech_recognition as sr


def user_input():
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = voice_recognizer.listen(source)

    user_text = voice_recognizer.recognize_google(audio, language="ru")
    print("Вы сказали: ", user_text)
    return user_text


def reply(text):
    print('Ответ: ', text)
    voice = gtts.gTTS(text, lang="ru")
    audio_file = "..\\audio.mp3"
    voice.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

text = user_input()
reply(text)