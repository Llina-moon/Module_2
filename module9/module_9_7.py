def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            return f"Результат {result} не является простым числом"
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f"Результат {result} составное число"
        return f"Результат {result} простое число"
    return wrapper



@is_prime
def sum_three(a,b,c):
    return a + b + c


result = sum_three(1, 3, 8)
print(result)
result = sum_three(1, 3, 3)
print(result)