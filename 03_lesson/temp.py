def convert_temperature():
  """Переводит температуру из Цельсия в Фаренгейт или наоборот."""
  choice = input("Выберите конвертацию (C - Цельсий в Фаренгейт, F - Фаренгейт в Цельсий): ")
  if choice.upper() == 'C':
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
  elif choice.upper() == 'F':
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} градусов Фаренгейта = {celsius} градусов Цельсия")
  else:
    print("Неверный выбор!")

# Пример использования
convert_temperature()
