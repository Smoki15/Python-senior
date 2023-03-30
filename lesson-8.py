result = []


def divider(a, b):
    try:
    if a < b:
        raise ValueError
    except IndexError as error:
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except ValueError as error:
for key in data:
    res = divider(key, data[key])
    result.append(res)
    print(result)
