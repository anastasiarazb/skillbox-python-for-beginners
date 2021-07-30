import playsound
import gtts
import os

text = 'Привет!'

voice = gtts.gTTS(text, lang="ru")
# Если возникает ошибка чтения файла - попробовать разные пути:
#  "audio.mp3", ".\\audio.mp3", абсолютный путь
audio_file = "..\\audio.mp3"
voice.save(audio_file)

playsound.playsound(audio_file)
# os.remove(audio_file)
