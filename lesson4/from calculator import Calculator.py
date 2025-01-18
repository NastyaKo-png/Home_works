from calculator1 import Calculator 

calculator1 = Calculator()

def test_sum_positive_nums(): #создали ранее в этом степе
    calculator1 = Calculator()
    res = calculator1.sum(4, 5)
    assert res == 9

def test_sum_negative_nums(): #создали ранее в этом степе
    calculator1 = Calculator()
    res = calculator1.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums(): #создали ранее в этом степе
    calculator1 = Calculator()
    res = calculator1.sum(-6, 6)
    assert res == 0

def test_sum_float_nums(): #проверка сложения десятичных дробей
    calculator1 = Calculator()
    res = calculator1.sum(5.6, 4.3)
    res = round(res, 1)  
    assert res == 9.9

def test_sum_zero_nums(): #проверка сложения целого числа и нуля
    calculator1 = Calculator()
    res = calculator1.sum(10, 0)
    assert res == 10

def test_div_positive(): #проверка деления чисел
    calculator1 = Calculator()
    res = calculator1.div(10, 2)
    assert res == 5

def test_div_by_zero(): #проверка деления на ноль
    calculator1 = Calculator()
    res = calculator1.div(10, 0)
    assert res == None 

def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
    calculator1 = Calculator()
    numbers = []
    res = calculator1.avg(numbers)
    assert res == 0

def test_avg_positive(): #проверка нахождения среднего для списка
    calculator1 = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator1.avg(numbers)
    assert res == 5