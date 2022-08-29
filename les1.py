age = input("Введите ваш возраст")
age1 = int(age)
if (age1) >= 100:
    print('you dead ')
elif  (age1)  >= 5 or (age1) == 10:
    print('мне ', age1, '  лет')
elif (age1) > 1 and (age1) < 5:
    print('мне ', age1, 'года')
elif (age1) == 1:
    print('мне ', age1, 'год')
else:
    print()
