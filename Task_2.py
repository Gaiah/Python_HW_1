## Задача 2: Найдите сумму цифр трехзначного числа.

user_number = int(input('Input some number: '))
sum = 0

while user_number > 0:
    sum += user_number % 10
    user_number //= 10

print(f'The sum of the digits of Your number is: {sum}')