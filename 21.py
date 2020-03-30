# 21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
# числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
# від 50 до 100.
# Гевчук Максим КН-А

from random import randint
from numpy import prod

arr = [randint(50, 100) for i in range(10)]
num = int(input('Введіть число:\n>>> '))
total = prod(tuple(filter(lambda x: x < num, arr)))
print(f'Масив елементів:\n{arr}\n'
      f'Сума елементів, які більші за {num}:\n{total}')