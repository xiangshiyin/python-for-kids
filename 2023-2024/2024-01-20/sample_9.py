class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I can not speak")

# a1 = Animal(name='an animal')
# print(a1.speak())

class dog(Animal):
    def bark(self):
        print("barking")
    
    def speak(self):
        print("I can bark")

    # def __init__(self, name):
    #     self.name = name

    # def speak(self):
    #     print("I can not speak")
d1 = dog(name='a dog')
print(d1.speak())
print(d1.bark())

class cat(Animal):
    def meow(self):
        print("meow...")
    
c1 = cat(name='a cat')
print(c1.meow())