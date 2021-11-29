def user_input():
    user_line = input('Введите текст: ')
    return user_line


def reply(text):
    print('Чего изволит хозяин:', text)


user_text = user_input()
user_text = user_text.lower()

if user_text == 'привет':
    reply('Привет-привет!')
elif user_text == 'пока':
    reply('Пока!')
elif user_text == 'закажи еду':
    reply('Пиццу или борщ')
else:
    reply('Не понятно, повторите')