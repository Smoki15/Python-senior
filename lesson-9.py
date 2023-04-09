my_list = [1, 2, 3]

my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# try:
#    print(next(my_iter))
# except StopIteration:
#    print('error')

for el in my_iter:
    print(el)

for el in my_iter:
    print(el)