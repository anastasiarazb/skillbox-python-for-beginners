counter = 5

while counter > 0:
    counter = counter - 1
    print('Counter =', counter)



# Если условие истинно всегда - цикл не оставистя до тех пор, пока мы не выйдем из программы

while True:
    user_input = input('Ваша реплика >>>')
    if user_input == 'пока':
        print('Пока-пока!')
        exit()


