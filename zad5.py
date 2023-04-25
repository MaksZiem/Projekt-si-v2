def decoration(func):
    def wrap():
        print("==================")
        print("a + b = ", func)
        print("==================")
    return wrap()

def suma(a,b):
    return a+b

decorated = decoration(suma(4,3))
