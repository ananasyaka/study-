def capitalize(func):
    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))
        print(result.upper())
    return wrapper

@capitalize
def plus(st1, st2):
    return (st1+st2)

plus("hello", "world")
