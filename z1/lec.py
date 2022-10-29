# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input(f'Введите вещественное число: ')
real_sum = 0
for n in number:
    if n.isdigit():
        real_sum+=int(n)
print(f'{number}    -> {real_sum}')