# #single inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# d1=Dog()
# d1.sound()
# d1.speak()

# #multiple inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Mammal:
#     def walk(self):
#         print("Mammal walks")
# class Dog(Animal,Mammal):
#     def speak(self):
#         print("Dog barks")
# d1=Dog()
# d1.sound()
# d1.walk()
# d1.speak()

# #multilevel inheritance
# class Animal:
#     def sound(self):
#         print("animal makes sounds")
# class Mamal(Animal):
#     def walk(self):
#         print("mamals walk")
# class Dog(Mamal):
#     def speak(self):
#         print("bark")

# d1=Dog()
# d1.sound()
# d1.walk()
# d1.speak()

# #hierarichal inheritance
# class Animal():
#     def sound(self):
#         print("animals make sound")
# class Dog(Animal):
#     def speak(self):
#         print("dof barks")
# class cat(Animal):
#     def speak(self):
#         print("cat say meow")
# d1=Dog()
# d1.sound()
# d1.speak()
# c1=cat()
# c1.sound()
# c1.speak()

# #hybrid inheritance
# class Animal():
#     def sound(self):
#         print("animals makes sounds")
# class Mamal():
#     def walk(self):
#         print("mamal can walk")
# class Dog(Animal,Mamal):
#     def barks(self):
#         print("dog barks")
# class Bat(Animal,Mamal):
#     def fly(self):
#         print("bat flies")
# class Flyingdog(Dog,Bat):
#     def do(self):
#         print("both walk and fly")

# f1=Flyingdog()
# f1.sound()
# f1.walk()
# f1.fly()
# f1.barks()
# f1.do()


#----------------

# #overloading and overriding:
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
#     def add(self,a,b,c,d):
#         return a+b+c+d
# c1=Calculator()
# print(c1.add(2,3))
# print(c1.add(2,3,4))
# print(c1.add(2,3,4,5))


# #overriding
# class Dog:
#     def sound():
#         print("bow bow")
# class Cat(Dog):
#     def sound():
#         print("meow meow") 
# c1=Cat()
# c1.sound()


#encapsulation
#public
class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def display(self):
        print("name:",self.name)
        print("model:",self.model)
c=Car("audi","a6")
c.display()
# #private
class Car:
    def __init__(self,name,model):
        self.__name=name
        self.__model=model
    def display(self):
        print("name:",self.__name)
        print("model:",self.__model)
c=Car("audi","a6")
c.display()

# # #protected
class Car:
    def __init__(self,name,model):
        self._name=name
        self._model=model
    def display(self):
        print("name:",self._name)
        print("model:",self._model)
c=Car("audi","a6")
c.display()