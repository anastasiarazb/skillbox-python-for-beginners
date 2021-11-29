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
    elif command == 'закажи еду':
        reply('Пиццу или борщ')
    else:
        reply('Не понятно, повторите')


user_text = user_input()
handle_command(user_text)
