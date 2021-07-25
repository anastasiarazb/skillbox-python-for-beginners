def user_input():
    # We will transform this function later to get voice
    user_line = input('Ваш текст: ')
    return user_line


def reply(text):
    # We will transform this function later to answer with voice
    print(text)


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
