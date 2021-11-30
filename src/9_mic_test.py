import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index,
                                                                                         name))
voice_recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Скажите что-нибудь >>>")
    audio = voice_recognizer.listen(source, phrase_time_limit=3)
    print("Голос записан")

with open('test_sound.wav', 'wb') as f:
    f.write(audio.get_wav_data())
