def user_input():
    user_line = input('Введите текст: ')
    return user_line


def reply(text):
    print('Чего изволит хозяин:', text)


def handle_command(command):
    command = command.lower()
    if command == 'привет':
        reply('Привет-привет!')
    elif command == 'пока':
        reply('Пока!')
        exit()
    elif command == 'закажи еду':
        reply('Пиццу или борщ')
    else:
        reply('Не понятно, повторите')


def start():
    while True:
        user_text = user_input()
        handle_command(user_text)

start()