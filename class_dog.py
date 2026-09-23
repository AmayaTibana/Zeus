class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def bark(self):
        print("Woof")

    def fetch(self):
        print(self.name, "went to fetch.")
my_dog = Dog("Flurry", "Ragdoll", 2, "Black")

print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)
print(my_dog.color)