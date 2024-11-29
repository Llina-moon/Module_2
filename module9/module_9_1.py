def apply_all_func(int_list, *functions):
    if not all(isinstance(item, (int, float)) for item in int_list):
        raise ValueError("Список должен содержать только числа (int, float)")

    result ={}
    for func in functions:
        name = func.__name__
        result[name] = func(int_list)
    return result


def min(int_list):
    result = int_list[0]
    for i in int_list:
        if i < result:
            result = i
    return result

def max(int_list):
    result = int_list[0]
    for i in int_list:
        if i > result:
            result = i
    return result

def sum_(int_list):
    return sum(int_list)

def sorted_(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))