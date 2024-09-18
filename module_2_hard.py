def generate_password(value):
    password = ""


    for i in range(1, value):
        for j in range(i + 1, value):
            summ = i + j


            if value % summ == 0:

                password += str(i) + str(j)

    return password

for value in range(3, 21):
    result = generate_password(value)
    print(f"Пароль для числа {value}: {result}")
