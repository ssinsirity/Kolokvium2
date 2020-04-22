# 55. У будинку, що складається з 30 квартир, переселити мешканців так, щоб мешканці першої квартири переїхали
# в тридцяту, з тридцятого - в першу, з другої - в 29 і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
# Гевчук Максим КН-А

from random import randint

arr = [randint(1, 6) for i in range(30)]  # створення масиву із к-стю мешканців, які проживають у квартирах
print('До переселення:')
print(*arr)
arr.reverse()  # "перевернення" масиву
print('Після переселення:')
print(*arr)
# фільтр, підрахунок та виведення
print(f'Кількість квартир, у яких проживає більше 5 осіб: {len(list(filter(lambda x: x > 5, arr)))}')