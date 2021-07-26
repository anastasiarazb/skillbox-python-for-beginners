import playsound
import gtts
import speech_recognition as sr
import os


def user_input():
    print("Скажите что-нибудь >>>")

    # We will transform this function later to get voice
    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Микрофон захвачен
        audio = voice_recognizer.listen(source)

    # Микрофон снова доступен другим программам

    voice_text = voice_recognizer.recognize_google(audio, language="ru")

    # Упражнение: добавить вывод текста
    print("Вы сказали:", voice_text)

    return voice_text


def reply(text):
    # Упражнение: добавить вывод текста
    print("Ассистент:", text)

    voice = gtts.gTTS(text, lang="ru")
    audio_file = "audio.mp3"
    voice.save(audio_file)

    playsound.playsound(audio_file)
    os.remove(audio_file)


def handle_command(user_text):
    if user_text == 'привет':
        reply('Привет-привет!')
    elif user_text == 'пока':
        reply('До скорого!')
        exit()  # <-- добавили сюда код выхода из функции
    elif user_text == 'закажи еду':
        reply('Пиццу или борщ?')
    else:
        reply("Не понимаю вас")


def start():
    while True:
        user_text = user_input()
        handle_command(user_text)


start()
