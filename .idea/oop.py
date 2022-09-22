class Animal:
    def __init__(self, name , age, sex ):
        self.name = name
        self.age = age
        self.sex = sex
    def hello(self):
        print('Кот '+ self.name)
    def hi(self):
        print('Ему '+ self.age)
    def goodbye(self):
        print("Он " + self.sex)

class Cat(Animal):
    def __init__(self, name="Борис", age="3", sex="кот"):
        super().__init__(name, age, sex)
    def sleep(self):
        print("спит ")

class Mouse(Animal):
    def __init__(self, name="Мини", age="1", sex="кошка"):
        super().__init__(name, age, sex)
    def eat(self):
        print("жрет")

class Jorge(Animal):
    def __init__(self, name="Жорик", age="11", sex="кот"):
        super().__init__(name, age, sex)
        self.name = name

    def dead(self):
        print("умер")