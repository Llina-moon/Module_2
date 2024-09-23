def print_params (a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()

print_params(b = 25)

print_params(c = [1,2,3])

values_list = (1,'hello' , 4.8)
print_params(*values_list)

values_dict = {"a": 5, "b" : 0.5, "c" : "wow" }
print_params(**values_dict)

values_list_2 = [True,87]
print_params(*values_list_2 ,42)