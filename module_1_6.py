my_dict = {"Catherine" : 1984 , "Elena" : 1986 , 'Sasha': 1988 ,'Nikolay': 1992}
print(my_dict)
print(my_dict['Nikolay'])
my_dict['Masha'] = 1993
print(my_dict['Masha'])
my_dict.update({'Anton' : 1992 , 'Viktor': 1972})
print(my_dict)
del my_dict['Anton']
print(my_dict)

my_set = {'Nikolay' , 1 ,9 ,1 ,2,8}
print(my_set)
my_set.add('Catherine')
print(my_set)
my_set.remove(9)
print(my_set)
