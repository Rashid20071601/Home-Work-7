my_dict = {'Rashid': 2007, 'Masha': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Rashid'))
print('Not existing value:', my_dict.get('Artem'))
my_dict.update({'Artem': 2000,
                'Andrey': 2009})
a = my_dict.pop('Rashid')
print('Deleted value:', a)
print('Modified dictionary: ', my_dict)

set_ = {1, 'Apple'}
print(f'Set: {set_}')
set_.remove(1)
set_.add(2)
print(f'Modified set: {set_}')