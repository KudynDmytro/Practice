#1.Найти все числа, что нацело делятся на 7 впромежутке от 1 до 50
z = input('enter a number:')


def first_ex(x):
    if x.isnumeric():
        for i in range(1, int(x)):
            if i % 7 == 0:
                print(i)
    else:
        print('Error: you entered not a number!')
        return


first_ex(z)


#2.Написать ИИ, который будет распознавать, что ввёл пользователь:e-mail, телефон или имя.
ent = input('enter:')


def lama(a):
    w = 'Sorry, I don\'t know what is that'
    if a[0] == '+':
        if len(a) == 13:
            if a[1:].isnumeric():
                if a[1:3] == '61':
                    print('You entered Australian phone number')
                elif a[1:3] == '43':
                    print('You entered Austrian phone number')
                elif a[1:5] == '1264':
                    print('You entered English phone number')
                elif a[1:4] == '375':
                    print('You entered Belorussian phone number')
                elif a[1] == '7':
                    print('You entered Russian phone number')
                elif a[1:4] == '380':
                    print('You entered Ukrainian phone number')
            else:
                print(w)
        else:
            print(w)
    else:
        if'@' in a:
            s = a.split('@')
            d = s[1].split('.')
            if '.' in s[0]:
                if s[0].count('.') > 1:
                    print(w)
                elif s[0][0] == '.':
                    print(w)
            else:
                if len(s[0]) >= 3:
                    if len(d[0]) == 3:
                        if len(d[1]):
                            print('You entered an e-mail')
        else:
            f = a.split(' ')
            if a.replace(' ', '').isalpha():
                for i in f:
                    if len(i) >= 2:
                        for j in i:
                            if j.isupper():
                                print('You entered a name')
                                return
                            else:
                                print(w)
                                break
                    else:
                        print(w)
                        break
            else:
                print(w)

lama(ent)
