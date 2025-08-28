# Polymorphism 
class Animal:
    def move(self):
        pass  # Abstract idea of movement

class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🦅"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"


# Vehicle Polymorphism
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# Test Polymorphism
animals = [Dog(), Bird(), Fish()]
vehicles = [Car(), Plane(), Boat()]

print("Animal Movements:")
for animal in animals:
    print(animal.move())

print("\nVehicle Movements:")
for vehicle in vehicles:
    print(vehicle.move())