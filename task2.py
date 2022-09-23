x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if (x == 0 or y == 0):
    print('Введите еще раз!')
elif(x > 0 and y >0):
    print('I четверть')
elif(x < 0 and y > 0):
    print('II четверть')
elif(x < 0 and y < 0):
    print('III четверть')
else:
    print('IV четверть')