# Задание 1. Сэт и сэт
my_set = set()
my_set.add(':)')
my_set.add(5)
my_set.add(0.0)
my_set_2 = set(['We', 'are', 'all', 'going', 'to', 'hell'])
union = my_set.union(my_set_2)
intersection = my_set.intersection(my_set_2)
diff = my_set.difference(my_set_2)
sym_diff = my_set.symmetric_difference(my_set_2)
my_set >= my_set_2
my_set <= my_set_2

# Задание 2. Словарик
dict = {}
dict['Literature'] = 4
dict['Biology'] = 5
dict['Geography'] = 3
dict['English'] = 4
dict['Physics'] = 2
dict['Math'] = 5
dict.pop('Biology')
dict['Literature']
for i in dict:
    print(dict[i])
for i in dict:
    n = i + 'ing'
    print(n)
for i in dict:
    print(i, dict[i])
for key, value in dict.items():
    print(key, value)
# Задание 3. Программа про строку
stroka = input('Введитe строку:')
if stroka[0].isupper():
    print('Строка начинается с большой буквы.')
if stroka[0].islower():
    print('Строка не начинается с большой буквы.')
print('Строка состоит из', len(stroka), 'букв.')
if stroka.endswith('!!'):
    print('Строка оканчивается на !!')
else:
    print('Строка не оканчивается на !!')
print('В строке сочетание букв "fire" встречается', stroka.count('fire'), 'раз.')
print('Так выглядит строка из всех больших букв:', stroka.upper())
print('Так выглядит строка из всех маленьких букв:', stroka.lower())
print('Так выглядит строка где каждое слово начинается с большой буквы:', stroka.title())
# Задание 4. Конвертация
# Из строки
my_str = 'abc'
my_list = [my_str]
my_set = {my_str}
my_tuple = (my_str,)
# Из списка
my_list = [1, 2, 3]
my_str = str(my_list)
my_set = set(my_list)
my_tuple = (my_list,)
# Из сэта
my_set = {'A', 'B', 'C'}
my_list = list(my_set)
my_str = str(my_set)
my_tuple = (my_set,)
# Из кортежа
my_tuple = (1, 2, 3)
my_str = str(my_tuple)
my_set = set(my_tuple)
my_list = list(my_tuple)
# Задание 5. Разворачиваем строку
# 5.1
a = '123456789'
list_a = list(a)
b = list_a[::-1]
c=''
for n in b:
    c += n
print(c)
# 5.2
a = '123456789'
list_a = list(a)
b = list_a[::-1]
c = ''
i = 0
while i < len(b):
    c += b[i]
    i += 1
print(c)
# 5.3
s = a[::-1]
print(s)
# Задание 6. Реверскомплементатор
a = input('Введите строку ДНК:')
b = list()
for i in a:
    if i == 'A':
        b.append('T')
    if i == 'T':
        b.append('A')
    if i == 'G':
        b.append('C')
    if i == 'C':
        b.append('G')
for n in b:
    print(n, end = '')