def counter(func):
     def wrapper(*args, **kwargs):
         wrapper.count += 1
         res = func(*args, **kwargs)
         print("Кол-во вызовов функции", func.__name__, ":", wrapper.count )
         return res
     wrapper.count = 0
     return wrapper

@counter
def double_string(string):
    print(string * 2)

double_string("ABC")