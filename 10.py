# 10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
# Визначити, скільки разів температура опускалася нижче -10 градусів.
# Гевчук Максим КН-А

arr = list(map(float, input('Введіть масив даних про температуру через пробіл:\n>>> ').split()))
count = len(list(filter(lambda x: x < -10, arr)))
print(f'Нижче -10 ℃ температура опускалась {count} разів')
