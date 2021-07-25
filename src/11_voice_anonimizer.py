import playsound
import gtts
import speech_recognition as sr


def user_input():
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


user_text = user_input()
reply(user_text)
