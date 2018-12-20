def tag(name):
    def wrapper(func):
        def inner():
            print ("<%s>" % name)
            func()
            print ("</%s>" % name)
        return inner
    return wrapper

@tag("b")
def hello():
    print ("Hello, world!")

hello()
