def divide( first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "Ошибка"



c = divide(23,5)

