from calculator import Calculator

calculator = Calculator()
# + +
# - -
# - +
# . .
# n 0

print ("start")
res = calculator.sum(4, 5)
assert res == 10

rer = calculator.sum(-6, -10)
assert res == -15
print ("finish")