def data_structure (lst):
    nums = []
    for item in lst:
        if isinstance(item,list):
            nums.extend(data_structure(item))
        elif isinstance(item, str):
          nums.append(len(item))
        elif isinstance(item, dict):
            for key, value in item.items():
                nums.extend(data_structure([key]))
                nums.extend(data_structure([value]))
        elif isinstance(item, tuple):
            nums.extend(data_structure(list(item)))
        elif isinstance(item, set):
            nums.extend(data_structure(list(item)))
        elif isinstance(item, (int, float)):
            nums.append(item)
    return nums
data = ([[1, 2, 3], {'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])])
numbers = data_structure(data)
summa = sum(numbers)
print(summa)

