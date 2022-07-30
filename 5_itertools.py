import itertools

a_list = [1, 2, 3]
b_list = ['a', 'b', 'c']

# itertools.product
print('\'itertools.product\' example:')
for a, b in itertools.product(a_list, b_list):
    print(f'{a},{b}')

# itertools.combinations
print('\n\'itertools.combinations\' example:')
for subset in itertools.combinations(a_list, 2):
    print(subset)
