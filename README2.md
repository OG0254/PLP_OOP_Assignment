# 🎭 Activity 2: Polymorphism Challenge

## 📖 Overview
This project demonstrates **Polymorphism** in Python OOP using different vehicle classes.  
Each vehicle implements the same method `move()` but behaves differently.

---

## 🏗️ Features
- **Car** → move() prints "Driving 🚗"
- **Plane** → move() prints "Flying ✈️"
- **Boat** → move() prints "Sailing 🚤"
- **Bicycle** → move() prints "Pedaling 🚴"

---

## 🔑 Code Example

```python
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
```

---

## 🚀 How to Run
1. Save the code into a file called `activity2.py`.
2. Run it with:
   ```bash
   python activity2.py
   ```
3. You’ll see how the same method `move()` behaves differently for each vehicle.

---

## 🎯 OOP Concept Demonstrated
- **Polymorphism** → The same method name (`move`) behaves differently depending on the class.

---

## ✅ Example Output
```
Car: Driving 🚗
Plane: Flying ✈️
Boat: Sailing 🚤
Bicycle: Pedaling 🚴
```

---

## 👨‍💻 Author
Created by **Ogada Brian** as part of a Python OOP assignment.
