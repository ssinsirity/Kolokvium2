# 19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
# остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
# здійснити випадковими числами від 200 до 300.
# Гевчук Максим КН-А

from random import randint

arr = [randint(200, 300) for i in range(20)]
total = sum(tuple(filter(lambda x: x % 2 == 3, arr)))
print(f'Масив елементів:\n{arr}\n'
      f'Сума елементів, у яких остача від ділення на 2 дорівнює 3:\n{total}')
