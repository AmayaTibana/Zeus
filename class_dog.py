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
my_dog1 = Dog("Fluffy","Beagle",2,"Brown")
my_dog2 = Dog("Mochi","Mutt",5,"White")
my_dog3 = Dog("Wolfie","Maltese",10,"Black")

print(my_dog2.name)
print(my_dog3.breed)
print(my_dog2.age)
print(my_dog.color)