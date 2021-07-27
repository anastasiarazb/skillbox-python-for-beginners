def user_input():
    print('Введите текст >>>')
    user_text = input()
    return user_text


def reply(text):
    # Завтра эту функцию перепишем так, чтобы она отвечала не текстом, а голосом
    print('Ответ:', text)

# Упражение (ДЗ №1): Код отсюда и ниже обернуть в функцию handle_command
# с одним аргументом user_text
# Также можно добавить больше реплик


def handle_command(user_text):
    user_text = user_text.lower()  # приведем текст к нижнему регистру

    if user_text == 'привет':
        reply('Привет-привет!')
    elif user_text == 'пока':
        reply("До скорого!")
    elif user_text == 'закажи еду':
        reply("Пиццу или борщ?")
    else:
        reply("Не понимаю вас")


user_text = user_input()
handle_command(user_text)