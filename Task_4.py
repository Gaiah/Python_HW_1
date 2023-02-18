# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?

user_num = int(input('Your number here: '))

if user_num % 2 == 0 and user_num % 3 == 0:
    print(f' Kate made {user_num // 3 * 2} origami cranes \n Peter and Sergei made {(user_num // 3) // 2} origami cranes each')
else: print('Incorrect number for this programm.')