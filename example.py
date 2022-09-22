def izmena(func):
    def wrapper(n):
        func(n.upper())
    return wrapper

@izmena
def name(n):
    print(f"Привет+ {n}")
name(input("Введите имя "))
