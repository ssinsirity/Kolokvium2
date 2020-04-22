# 27. Лінійний масив містить відомості про кількість опадів, що випали за кожен з 12 місяців одного року.
# Складіть програму, що визначає загальну кількість опадів протягом цього року, середньомісячну кількість опадів,
# кількість посушливих місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
# Гевчук Максим КН-А

months = ['Січень', 'Лютий', 'Березень', ' Квітень', 'Травень', ' Червень', ' Липень', ' Серпень', ' Вересень',
          ' Жовтень', 'Листопад', 'Грудень']
print('Введіть к-сть опадів за кожний місяць:')
arr = [float(input(f'{mon}: ')) for mon in months]
# виведення
print(f'\nЗагальна кількість опадів: {sum(arr)} мм\n'
      f'Середньомісячна к-сть опадів: {sum(arr) / 12:.1f} мм\n'
      f'К-сть посушливих місяців: {len([x for x in arr if x < 30])}\n'
      f'Найпосушливіший місяціь: {months[arr.index(min(arr))]}')