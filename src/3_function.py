def user_input():
    user_line = input('Введите текст: ')
    return user_line

def reply(text):
    print('Вы сказали:', text)


command = user_input()
reply(command)
