def raise_to_the_degress(number, max_degree):
    i = 0

    for _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_to_the_degress(122345, 500)
print(res)

for _ in res:
    print(_)