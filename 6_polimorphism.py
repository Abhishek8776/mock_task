# Write a Python program demonstrating polymorphism.
"""
in python the the polymorphism is mainly 4 types
1.operator overloadig
2.duck typing
3.method overloading
4.method overriding
"""

# operator overloading
print(1 + 2)
print("a" + "b")


# duck typing
class Dog:
  def speak(self):
    return "Bow"
class Cat:
  def speak(self):
    return "Meow"
def animal_sound(animal):
  return animal.speak()
dog = Dog()
cat = Cat()
print(animal_sound(dog))
print(animal_sound(cat))


#method overloading
class Addition:
  def adding(self,*args):
    return sum(args)
a=Addition()
print(a.adding(3,4))
print(a.adding(3,4,5))

#method overriding
class Father:
  def sleep(self):
    return "sleeps from 10pm to 6am"
class Child(Father):
  def sleep(self):
    return "sleeps from 12pm to 8am"
ch=Child()
print(ch.sleep())