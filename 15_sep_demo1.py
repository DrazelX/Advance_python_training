def outer(f):
    def inner():
        result = f()
        return result ** 2
    return inner

@outer
def num():
    return 5

print(num())