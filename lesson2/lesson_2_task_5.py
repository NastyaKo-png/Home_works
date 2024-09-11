def month_to_season(month):
  """
  Функция возвращает название сезона, соответствующего номеру месяца.

  Args:
    month: Номер месяца (целое число от 1 до 12).

  Returns:
    Название сезона (строка).
  """
  if 3 <= month <= 5:
    return "Весна"
  elif 6 <= month <= 8:
    return "Лето"
  elif 9 <= month <= 11:
    return "Осень"
  else:
    return "Зима"

# Примеры использования функции
print(month_to_season(2)) # Вывод: Зима
print(month_to_season(5)) # Вывод: Весна
print(month_to_season(8)) # Вывод: Лето
print(month_to_season(11)) # Вывод: Осень
