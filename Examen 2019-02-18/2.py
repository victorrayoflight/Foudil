def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier

a = Foo(5)
b = Foo(5)

print(a(b(4)))