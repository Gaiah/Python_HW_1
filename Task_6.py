# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. \
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.


ticket_number = int(input('Ticket\'s  six-digit number: '))

first_sum = 0
second_sum = 0
count = 6

while count > 0:
    if count > 3:
        second_sum += ticket_number % 10
        ticket_number //= 10
        count -= 1
    else:
        first_sum += ticket_number % 10
        ticket_number //= 10
        count -= 1

if first_sum == second_sum:
    print('Congratulations! You got lucky ticket!')
else:
    print('Oops! Better luck next time. :)')