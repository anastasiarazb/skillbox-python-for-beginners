# ДЗ 2 (конкурсное)

# Добавить в чат-бота голосовой интерфейс
# Добавить к каждой функции комментарий с описанием того, что делает эта функция

# ДЗ копируется в файл ideone.com (аналогично тому, как мы делали в 1-й день), ссылка на файл
# присылается в Google Forms, которая будет закреплена в телеграм-чате

# ДЗ считается выполненным, если
# 1) сделаны какие-то попытки его выполнить (неважно - код работает или нет,
# запускается ли он с ошибками или нет) - если вы попытались написать сами какой-то код -
# это считается
# 2) ДЗ открывается (вы прислали ссылку на открытый к просмотру файл и это ваш файл,
# а не общая ссылка ideone.com)
# 3) Только при наличии комментариев к коду

# Т.е. если понятно, что была попытка довести чат-бот до конца, даже если с реализацией что-то
# не получилось

# Дедлайн: 19 часов по МСК

import playsound
import gtts
import os
import speech_recognition as sr


def user_input():
    print("Скажите что-нибудь >>>")
    voice_recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
        # voice_recognizer.adjust_for_ambient_noise(source, duration=5)
            audio = voice_recognizer.listen(source)

        user_text = voice_recognizer.recognize_google(audio, language="ru")
        print("Вы сказали: ", user_text)
        return user_text
    except sr.UnknownValueError:
        print("Ошибка распознавания :(")


def reply(text):
    print('Ответ: ', text)
    voice = gtts.gTTS(text, lang="ru")
    audio_file = "..\\audio.mp3"
    voice.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def handle_command(user_text):
    user_text = user_text.lower()  # приведем текст к нижнему регистру

    if user_text == 'привет':
        reply('Привет-привет!')
    elif user_text == 'пока':
        reply("До скорого!")
        exit()
    elif user_text == 'закажи еду':
        reply("Пиццу или борщ?")
    else:
        reply("Не понимаю вас")


def start():
    user_text = user_input()
    handle_command(user_text)


while True:
    try:
       start()
    except:
        reply("Какая-то ошибка")
        exit()
