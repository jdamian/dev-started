# Parent class
class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
    
    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
        # return self.name, self.age

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
        # return "%s says %s" % (self.name, sound)
    
    # Instance method
    def eat(self):
        self.is_hungry = False
    
    def walk(self):
        return "%s is walking!" % (self.name)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
        # return "%s runs %s" % (self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
        # return "%s runs %s" % (self.name, speed)

# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# Is julie and instance of jim?
print(isinstance(julie, jim))

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
print("And they're all {}s, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

my_pets.walk()
