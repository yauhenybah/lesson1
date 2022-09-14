r = 0
a = 0
b = 0
c = 0
h = 0
def krug(r):
    r = int(input("Введите радиус круга "))
    return 3.14 * r**2

def priam(a,b):
    a = int(input("Введите сторону а "))
    b = int(input("Введите сторону b "))
    return a * b
def tri(c,h):
    c = int(input("Введите осование "))
    h = int(input("Введите высоту "))
    return (c*h)/2
vibor = input("Сделате ваш выбор (k, p, t) ")
print(vibor)
if vibor == "k":

    print("Площадь круга =", krug(r))
elif vibor == "p":
    print("Площадь прямоугольника =", priam(a,b))
elif vibor == "t":
    print("Площадь треугольника =", tri(c,h))
else:
    print("Не верный ввод")
