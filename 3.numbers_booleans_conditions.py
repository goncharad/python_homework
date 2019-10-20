# Задание 1. Преобразования между int, float и str
# 1
a = 2
print(float(a))
print(str(a))

b = 4.5
print(int(b))
print(str(b))

c = '10'
print(int(c))
print(float(c))
# 2
a = -5
print(float(a))
print(str(a))

b = 0.33
print(int(b))
print(str(b))

c = '-2'
print(int(c))
print(float(c))
# 3
a = 0
print(float(a))
print(str(a))

b = 0.11111111111111111111111111111111111
print(int(b))
print(str(b))

c = '0'
print(int(c))
print(float(c))
# 4
a = 1234567890
print(float(a))
print(str(a))

b = 1/3
print(int(b))
print(str(b))

c = '5'
print(int(c))
print(float(c))
# 5
a = 20/10
print(float(a))
print(str(a))

b = 1/10
print(int(b))
print(str(b))

c = '-8'
print(int(c))
print(float(c))

# Задание 2. 3 формулы по 3 примера
H = float(input('Введите высоту цилиндра:'))
R = float(input('Введите радиус цилиндра:'))
square_of_cylinder = 2*3.14*R*H + 2*3.14*(R**2)
print('Площадь цилиндра:', round(square_of_cylinder,2))

H_1 = 10
R_1 = 100
print(2*3.14*R_1*H_1 + 2*3.14*(R_1**2))

H_2 = 0.2
R_2 = 0.01
print(2*3.14*R_2*H_2 + 2*3.14*(R_2**2))

H_3 = 3
R_3 = 5
print(2*3.14*R_3*H_3 + 2*3.14*(R_3**2))

X_0 = float(input('Введите начальную координату:'))
V = float(input('Введите скорость:'))
t = float(input('Введите время:'))
X = X_0 + V*t
print('Конечная координата:', round(X,2))

X_0 = 4.0
V = 5.5
t = 0.0
print(X_0 + V*t)

X_0 = 0.0
V = 3.7
t = 0.33333
print(X_0 + V*t)

X_0 = 1111.1
V = 0.0
t = 10000000.0
print(X_0 + V*t)

height = float(input('Введите высоту правильной шестиугольной призмы:'))
side = float(input('Введите сторону правильной шестиугольной призмы:'))
vol_of_regular_hexagonal_prism = 1.5*(side**2)*height*(3**(0.5))
print('Объем правильной шестиугольной призмы:', round(vol_of_regular_hexagonal_prism,2))

height_1 = 1.0
side_1 = 1.0
vol_1 = 1.5*(side_1**2)*height_1*(3**(0.5))
print(vol_1)

height_2 = 0.0
side_2= 0.0
print(1.5*(side_2**2)*height_2*(3**(0.5)))

height_3 = 10000.0
side_3 = 0.33333
print(1.5*(side_3**2)*height_3*(3**(0.5)))

# Задание 3. Таблицы истинности
# not
print('','a', '\t', '\t', 'not a', '\n', True,'\t', not True, '\n', False,'\t', not False)
# or
print('','a', '\t', '\t', 'b', '\t','\t', 'a or b', '\n', True,'\t', False,'\t', (True or False),'\n', False,'\t', True, '\t',(False or True),'\n', True, '\t', True, '\t', (True or True),'\n', False, '\t', False, '\t', (False or False))
# xor
print('','a', '\t', '\t', 'b', '\t', '\t', 'a xor b')
print(True, '\t', False, '\t', ((True and not False) or (not True and False)))
print(False, '\t', True, '\t', ((False and not True) or (not False and True)))
print(True, '\t', True, '\t', ((True and not True) or (not True and True)))
print(False, '\t', False, '\t', ((False and not False) or (not False and False)))
# nor
print('','a', '\t', '\t', 'b', '\t', '\t', 'a nor b')
print(True, '\t', False, '\t', not(True or False))
print(False, '\t', True, '\t', not(False or True))
print(True, '\t', True, '\t', not(True or True))
print(False, '\t', False, '\t', not(False or False))
# and
print('','a', '\t', '\t', 'b', '\t', '\t', 'a and b')
print(True, '\t', False, '\t', True and False)
print(False, '\t', True, '\t', False and True)
print(True, '\t', True, '\t', True and True)
print(False, '\t', False, '\t', False and False)
# nand
print('','a', '\t', '\t', 'b', '\t', '\t', 'a nand b')
print(True, '\t', False, '\t', not(True and False))
print(False, '\t', True, '\t', not(False and True))
print(True, '\t', True, '\t', not(True and True))
print(False, '\t', False, '\t', not(False and False))

# Задание 4. Fizz buzz
a = int(input('Введите целое число:'))
if a % 15 == 0:
    print('fizzbuzz')
elif a % 3 == 0:
    print('fizz')
elif a % 5 == 0:
    print('buzz')
else:
    print(a)