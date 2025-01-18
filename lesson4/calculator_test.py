from calculator import Calculator
calculator = Calculator ()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, -10) #поменяли параметры
    assert res == 789 #поменяли ожидаемую сумму

def test_sum_positive_and_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, 6) #поменяли параметры
    assert res == 7 #поменяли ожидаемую сумму
