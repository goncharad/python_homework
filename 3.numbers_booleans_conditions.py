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
H = float(input())
R = float(input())
square_of_cylinder = 2*3.14*R*H + 2*3.14*(R**2)
print(square_of_cylinder)

H_1 = 10
R_1 = 100
print(2*3.14*R_1*H_1 + 2*3.14*(R_1**2))

H_2 = 0.2
R_2 = 0.01
print(2*3.14*R_2*H_2 + 2*3.14*(R_2**2))

H_3 = 3
R_3 = 5
print(2*3.14*R_3*H_3 + 2*3.14*(R_3**2))

X_0 = float(input())
V = float(input())
t = float(input())
X = X_0 + V*t
print (X)

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

height = float(input())
side = float(input())
vol_of_regular_hexagonal_prism = 1.5*(side**2)*height*(3**(0.5))
print(int(vol_of_regular_hexagonal_prism))

height_1 = 1.0
side_1 = 1.0
vol_1 = 1.5*(side_1**2)*height_1*(3**(0.5))
print(vol_1) # не получилось тут вывод сделать в виде int

height_2 = 0.0
side_2= 0.0
print(1.5*(side_2**2)*height_2*(3**(0.5)))

height_3 = 10000.0
side_3 = 0.33333
print(1.5*(side_3**2)*height_3*(3**(0.5)))

# Задание 3. Таблицы истинности

