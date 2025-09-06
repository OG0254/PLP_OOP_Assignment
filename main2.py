# Activity 2: Polymorphism Challenge! 🎭

# Base Class
class Vehicle:
    def move(self):
        pass  # placeholder method


# Subclasses with their own implementation of move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"


# Example Usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for v in vehicles:
        print(f"{v.__class__.__name__}: {v.move()}")
