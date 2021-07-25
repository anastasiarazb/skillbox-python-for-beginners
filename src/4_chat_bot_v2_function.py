def user_input():
    # We will transform this function later to get voice
    user_line = input('Ваш текст: ')
    return user_line


def reply(text):
    # We will transform this function later to answer with voice
    print(text)


user_text = user_input()

if user_text == 'привет':
    reply('Привет-привет!')
elif user_text == 'пока':
    reply('До скорого!')
elif user_text == 'закажи еду':
    reply('Пиццу или борщ?')
else:
    reply("Не понимаю вас")
