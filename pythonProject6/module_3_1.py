
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string) , string.upper() ,string.lower()

result = string_info('Baracuda')
result2 = string_info('nub')
print(result,result2)

def is_contains(string ,list_to_search):
    count_calls()
    lower_string = string.lower()
    for item in list_to_search:
        if lower_string == item.lower():
            return True


    return False

my_string = 'СтРоКа'
my_string2 = 'Помогите'
my_list = ['строка', 'в', 'искомОм', 'СПИСКЕ']

result = is_contains(my_string, my_list)
result2 = is_contains(my_string2, my_list)
print(result,result2)


print(f'Количество вызовов:{calls}')



