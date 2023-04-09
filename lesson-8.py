result = []



def divider(a, b):
    result = 0
    try:
        result = a / b
    except ValueError:
        print("ValueError")
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return result

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
try:
for key in data:
    res = divider(key, data[key])
    result.append(res)
    print(result)
