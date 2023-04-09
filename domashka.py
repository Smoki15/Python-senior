def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems{exc}")
        else:
            print(f"No problems. Result - {result}")


    return checker


def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate("2+2*2+2")
calculate("10-5+10")
calculate("4+5+1*5")
calculate("6+6+5+4+2")
calculate("5+2+1+6*7")