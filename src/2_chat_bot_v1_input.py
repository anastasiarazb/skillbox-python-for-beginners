print('Введите команду:')
user_text = input()

user_text = user_text.lower()

if user_text == 'привет':
    print('Привет-привет!')
elif user_text == 'пока':
    print('Пока!')
elif user_text == 'закажи еду':
    print('Пиццу или борщ')
else:
    print('Не понятно, повторите')