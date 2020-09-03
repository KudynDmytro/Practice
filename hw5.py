import numpy as nu
'''
1.Написать функцию, принимающую два аргумента.
Если оба аргумента являются числами - вернуть их произведение, если строками - собрать в одну строку и вернуть,
если первый строка, а второй нет - вернуть словарь, в котором ключ - первый аргумент, значение - второй.
'''
a = input('enter a:')
b = input('enter b:')
def first(x,y):
    if x.isnumeric() and y.isnumeric():
        return int(x)*int(y)
    elif x.isalpha() and y.isalpha():
        return x + y
    elif x.isalpha() and y.isalpha() == False:
        s ={x : y}
        return s

print(first(a, b))

'''
2.Дан словарь продавцов и цен на iphone xs max 256gb у разных продавцов на hotline: 
{ ‘citrus’: 47.999, ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988, ‘sota’: 37.720 },
написать функцию возвращающую список имен продавцов, чьи цены попадают в диапазон (from_price, to_price).
'''
m = { 'citrus': 47.999, 'istudio': 42.999, 'moyo': 49.999, 'royal-service': 37.245, 'buy.ua': 38.324, 'g-store': 37.166, 'ipartner': 38.988, 'sota': 37.720 }
price1 = input('enter lower price:')
price2 = input('enter higher price:')
def second(n, k):
    q = float(n)
    w = float(k)
    final = []
    for i in m.items():
        r = list(i)
        if r[1] in nu.linspace(q, w):
            final.append(r[0])
    return final

second(price1, price2)

'''
3.Пользователь вводит строку произвольной длины. 
Написать функцию, которая должна вернуть словарь следующего содержания:
{

"0": количество пробелов в строке

"1": list слов из одной буквы

"2": list слов из дву букв  

"3": list слов из трех букв
...

"punctuation" : tuple уникальных знаков препинания

}
'''
string = input('enter a string:')
def third(o):
    signs = '.,?!:;()""'
    one_let = []
    two_let = []
    three_let = []
    uniq = set()
    for q in o:
        if q in signs:
            uniq.add(q)
    for i in [o.split(' ')]:
        for j in i:
            if len(j) == 1:
                one_let.append(j)
            if len(j) == 2:
                two_let.append(j)
            if len(j) == 3:
                three_let.append(j)

    keys = ["0", "1", "2", "3", "punctuation"]
    values =[o.count(' '), one_let, two_let, three_let, tuple(uniq)]
    return dict(zip(keys, values))

third(string)