# 7. Створіть масив А [1..12] за допомогою генератора випадкових чисел з
# елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
# масиву числом 0.
# Гевчук Максим КН-А
import numpy as np

arr = np.array([np.random.randint(-20, 10) for i in range(12)])
print(f'Масив з елементами:\n{arr}')
for elem in range(len(arr)):
    if arr[elem] < 0:
        arr[elem] = 0
print(f'Масив із зміненими елементами:\n{arr}')