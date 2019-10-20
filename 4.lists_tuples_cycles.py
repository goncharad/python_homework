# Задание 1. Играемся со списком.
# Создали
my_training_list = list()
# Добавили элементы
my_training_list.append(0.5)
my_training_list.append('Word')
my_training_list.append(1)
# Добали к нему другой список
another_list = ['hello', ',', 'world', '!']
my_training_list.extend(another_list)
# Удалили элементы
my_training_list.remove(0.5)
my_training_list.remove(1)
# Задали элемент с индексом 1
my_training_list[1] = 10
# Посчитали количество вхождений одного из элементов
my_training_list.count(',')
# Посчитали длину
len(my_training_list)
# Задание 2. Играемся со кортежем.
# Создали
my_training_tuple = tuple(['hello', ',', 'world', '!'])
# Посчитали количество вхождений одного из элементов
my_training_tuple.count(',')
# Посчитали длину
len(my_training_tuple)
# Вот и все :(
# Задание 3. Поприветствуем друзей.
friends = ['Anna', 'Julia', 'Taisia', 'Kate', 'Maria', 'Marina']
for name in friends:
    print('Hi,', name)
print('Hi, everyone!')
# Задание 4. Складываем коллекции.
list1 = [1, 2, 3, 4, 5]
list2 = [-1, -2, -3, -4, -5]
list3 = []
n = 0
for number in list1:
    a = [list1[n] + list2[n]]
    list3.append(a)
    n += 1
list3
# Задание 5. Определяем тип треугольника.
a = float(input())
b = float(input())
c = float(input())
if a + b != c and a + c != b and b + c != a:
    if a == b == c:
       print('Треугольник равносторонний!')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный!')
    else:
        print('Треугольник разносторонний!')
else:
    print('Такого треугольника не существует!')
# Задание 6. Разворачиваем лист.
# Способ 1
elements = [1, 2, ('fruit', 5)]
print(elements[::-1])
# Способ 2
elements_copy = [1, 2, ('fruit', 5)]
elements_copy.reverse()
print(elements_copy)
# Задание 7. Считаем сумму четных чисел кортежа
interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37)
s = 0
    for element in interesting_numbers:
        if element % 2 == 0:
            s += element
print(sum)
