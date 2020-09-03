'''
1.Попросить пользователя ввести строку.
Определить длину введенной пользователем строки.
добавить полученную длину к строке (“string ‘abcd’ has [длина] symbol(s)”)
'''

new_str = input('write something in here:')
length = len(new_str)
print(f'string {new_str} has {length} symbol(s)')

'''
2.Попросить пользователя ввести строку произвольной длины. 
Попросить пользователя ввести одно слово. 
Определить входит ли в строку переданное пользователем слово (учтите, что слова могут начинаться с большой буквы).
'''
any_str = input('write srting of any length:')
any_word = input('write any word:')
is_in = any_word in any_str
if is_in:
    print(f'word "{any_word}" attends in \"{any_str}\"')
else:
    print(f'word "{any_word}" doesn\'t attend in \"{any_str}\"')

'''
3.Пользователь вводит строку произвольной длины. 
Определить количество слов , которые начинаются на "а".
'''
any_str = input('write srting of any length:')
massive = list(any_str.split())
i = 0
num = 0
for i in range(len(massive)):
    if massive[i][0] == 'a':
        num += 1
print('Amount of words, which start from "a":',num)


'''
4.Попросить пользователя ввести свой возраст. 
-если пользователю меньше 10 - вывести “где твои мама и папа?”
-если пользователю меньше 18 - вывести “мы не продаем алкоголь несовершеннолетним”
-если пользователю больше 70 - вывести “вам в пенсионный отдел”
-в любом другом случае - вывести “добро пожаловать, товарищ!”
'''

age = input ('введите свой возраст :')
int_age = int(age)
if (int_age < 10):
    print('где твои мама и папа?')
elif (int_age < 18 ):
    print('мы не продаем алкоголь несовершеннолетним')
elif (int_age > 70):
    print('вам в пенсионный отдел')
else:
    print('добро пожаловать, товарищ!')




