def personal_sum(numbers):
    numb = 0
    incorrect_data = 0

    for i in numbers:
        try:
            numb += i
        except TypeError :
            incorrect_data += 1
            print(f'Не корректный тип данных')

    return numb, incorrect_data

#print(personal_sum([2,3,4,"hgn"]))

def calculate_average(numbers):
    try:
        if not isinstance(numbers,(list,tuple,set)):
            raise TypeError('не является коллекцией')

        total_sum,incorrect_sum = personal_sum(numbers)

        if len(numbers) - incorrect_sum == 0:
            return 0

        return total_sum / (len(numbers) - incorrect_sum)

    except TypeError:
        print("не верный тип данных")
        return None

    except ZeroDivisionError:
        return 0

#print(calculate_average([2,3,4,"hgn"]))
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

