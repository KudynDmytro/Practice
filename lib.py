def num():
    w = input('enter:')
    while True:
        if w.isnumeric():
            print(int(w))
            return int(w)
        else:
            w = input('error, try again:')


def out_rec(dct):
    for itm1 in dct.items():
        if type(itm1[1]) == dict:
            return out_rec(itm1[1])
        else:
            print(itm1)


def soul(lst):
    b = {lst[i]: type(lst[i]) for i in range(0, len(lst))}
    print(b)

d = {
     'needle': 234,
     'honor': 'fiends grip',
      234: {
          'axe': 3,
          'temple': 'run',
          'see': {
             'strength': 12,
             'agility': 21
        }
           }
     }

l = [123, 22, 'saber', 'people', (1, 2, 3, 4), 'echo']

user = {
    'name':'Alisher Morgenstern',
    'birthday date': '17.02.1998',
    'car': 'Mercedes'
}

def empty(dct):
    date = input("enter today's date:")
    q = date.split('.')
    for i in dct.values():
        if i[0].isnumeric():
            e = i.split('.')
            if e[0] == q[0] and e[1] == q[1]:
                value = list(dct.values())
                print(f'Happy birthday {value[0]}!')

