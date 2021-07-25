def user_input():
    user_line = input('Ваш текст: ')
    return user_line


def reply(text):
    print(text)


user_text = user_input()
reply(user_text)

