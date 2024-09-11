def is_year_leap(year):
  """
  Функция определяет, является ли год високосным.

  Args:
    year: Год (число).

  Returns:
    True, если год високосный, и False - если иначе.
  """
  if year % 4 == 0:
    return True
  else:
    return False

# Вызов функции и сохранение результата
year = 2024
is_leap = is_year_leap(year)

# Вывод результата
print(f"год {year}: {is_leap}")
