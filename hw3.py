'''
1.Написать алгоритм перехода через улицу.
Ваш робот стоит на одной стороне уkицы и должен попасть на другую сторону по пешеходному переходу.
Робот может шагать вперед, смотреть по сторонам и вперед.
Можно описать как угодно, хоть блок-схемой, хоть текстом, главное понятно.
'''
command1 = 'step'
command2 = 'lookL'
command3 = 'lookR'
command4 = 'lookA'
i = 0
a = 0
b = 2
for i in range(a, b):
    choice = input('enter a command(step,lookL,lookR,lookA):')
    if choice == command1:
        i += 1
        print(b - i, 'steps left')
        if b - i == 0:
            print('you crossed the street!')
    elif choice == command2:
        print('you looked left')
    elif choice == command3:
        print('you looked right')
    elif choice == command4:
        print('you looked ahead')
    else:
        print('wrong input, try again')


'''
2.Пользователь вводит строку произвольной длины.
Найти в строке самое длинное слово, в котором присутствуют подряд две согласные буквы.
Если в строке присутствует слово с тремя согласными буквами подряд - завершить выполнение.
'''
mas = 'bcdfghjklmnpqrstvwxz'
write = input('enter something:')
lst = write.split()
word = 0
for i in range(0, len(lst)):
    try:
        if lst[i][i] and lst[i][i + 1] and lst[i][i + 2] in lst and mas.split():
            break
        else:
            for i in range(0, len(lst)):
                if len(lst[word]) < len(lst[i]):
                    word = i
                    if lst[word][i] and lst[word][i + 1] in mas:
                        print(lst[word])
            break
    except:
        print(Exception)
        break


"""
3.Попросить пользователя ввести с клавиатуры строку и вывести ее на экран.
Спросить у пользователя, хочет ли он повторить операцию (Y/N)?.
Повторять операцию если (Y), завершить выполнение если (N), если ответ не Y или N -  переспрашивать, пока не введет Y или N.
"""
write = input('enter something:')
print(write)
ask = input('do you want to repeat an operation?(Y/N)')
while ask != 'Y' or 'N':
    ask = input('do you want to repeat an operation?(Y/N)')
    if ask == 'Y':
        write = input('enter something:')
        print(write)
    elif ask == 'N':
        break
