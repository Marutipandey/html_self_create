print("hello")


x=lambda a:a+10
print(x(5))


def num(b):
    return lambda a:a*b
hello=num(5)
print(hello(20))


