lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Цикл по элементам списка
for num in lst:
  # Проверка условий: меньше 30 и делится на 3 без остатка
  if num < 30 and num % 3 == 0:
    print(num)
