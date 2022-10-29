# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число:'))
i = 2
d = round((1+1/n)**n)
p = {1:(1+d)}
while i != n+1:
    res = p.get(i-1)+d
    p.update({i:res})
    i+=1
print(p)

