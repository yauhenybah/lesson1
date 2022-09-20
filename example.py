def izmena(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        val = val.upper() + "!"
        return val
    return wrapper()

#@izmena
def name(a):
    print("Привет " + a)
name(input("Введите имя "))
