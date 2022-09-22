from abc import abstractmethod
class Animal:
    def __init__(self):
        pass
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def clas(self):
        pass

    @abstractmethod
    def name(self):
        pass

class Tiger():
    def __init__(set):
        pass
    def type(self):
        print("Tiger")
    def clas(self):
        print("Predator")
    def name(self):
        print("Bengal")

class Hear():
    def __init__(set):
        pass
    def type(self):
        print("Hear")
    def clas(self):
        print("Herbivore")
    def name(self):
        print("Rusak")

tiger1 = Tiger()
tiger1.type()
tiger1.clas()
tiger1.name()

hear1 = Hear()
hear1.type()
hear1.clas()
hear1.name()
