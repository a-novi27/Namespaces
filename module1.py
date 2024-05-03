import math


def test_function():
    print('Я внешняя функция')

    def inner_function():
        print('"Я в области видимости функции test_function"')
    inner_function()

test_function()

    # inner_function() - не работает








    








