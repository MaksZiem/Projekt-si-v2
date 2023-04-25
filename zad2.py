x = input("podaj x: ")


for i in range(1, int(x)+1):
    result = lambda a: a ** 2
    print(result(i))
