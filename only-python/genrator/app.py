my_number = (x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9])  # genrator


def gentatorFunction():
    i = 0
    while i < 10:
        yield i
        i += 1


g = gentatorFunction()
print(next(g))
print(next(g))
print(list(g))
print(list(my_number))


friends = ['umesh', 'Aku', 'Aditi', 'Kundan', 'Yash', 'Ashu']

start_with_r = filter(lambda friend: friend.startswith('A'), friends)

print(list(start_with_r))
