def fizz_buzz(n):
  """
  Функция печатает числа от 1 до n с заменой кратных 3 на "Fizz", 
  кратных 5 на "Buzz", а кратных 3 и 5 на "FizzBuzz".

  Args:
    n: Верхняя граница диапазона чисел.
  """
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# Вызов функции fizz_buzz
fizz_buzz(15)
