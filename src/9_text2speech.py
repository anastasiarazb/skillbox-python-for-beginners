import playsound
import gtts


text = 'Привет!'

voice = gtts.gTTS(text, lang="ru")
audio_file = "audio.mp3"
voice.save(audio_file)

playsound.playsound(audio_file)
