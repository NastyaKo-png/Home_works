import math

def square(side):
  """
  Функция вычисляет площадь квадрата.

  Args:
    side: Длина стороны квадрата (число).

  Returns:
    Площадь квадрата (число).
  """
  area = side * side
  # Округление площади вверх, если сторона не целое число
  if not isinstance(side, int):
    area = math.ceil(area)
  return area

# Примеры использования функции
print(square(5)) # Вывод: 25
print(square(3.5)) # Вывод: 13
