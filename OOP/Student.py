# class Student:
#     name="Yash"
#     age=20


# S= Student()
# print(S.name)
# print(S.age)
# S.name="Pikachu"
# print(S.name)

class Person:
    name="yash"
    age=20
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __init__(self):
        pass
    
    def talk(self):
        print(f'{self.name} is talking')

obj=Person()
print(obj.name)
print(obj.age)
print(obj.talk())
