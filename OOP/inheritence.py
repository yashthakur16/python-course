class Animal:
    def walk(self):
        print("The animal is walking")

class Cat(Animal):
    pass

class Dog(Animal):
    def walk(self):
        print("The Dog is walking")


def add(x,y):
    return x+y


obj=Dog()
obj.walk()