def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1
print_params()
print_params(15, False)
print_params(15, False, False)
print_params(b = 25)
print_params(c = [1,2,3])

# 2
values_list = [73.36, 'Строка_2', True ]
values_dict = {'a': 24, 'b': 'строка_3', 'c': False}

print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [55.34, 'Строка_4']
print_params(*values_list_2, 46)