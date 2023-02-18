# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Input size N for the chocolate: '))
m = int(input('Input size M for the chocolate: '))

if (n*m) % 2 != 0:
    print('The product of N and M should be even. Please restart the programm for it\'s correct work! ')
else:
    k = int(input('How many pieces of chocolate do you want? : '))
    if k % 2 == 0:
        print('Bon apetite!')
    else:
        print(f'You can’t part the chocolate into {k} and {n * m - k} pieces.')