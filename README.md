# 📱 Smartphone Class - Python OOP Assignment

## 📖 Overview
This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python by creating a class that represents a **Smartphone**.  
It covers:
- Classes & Objects  
- Constructors (`__init__`)  
- Inheritance  
- Encapsulation  
- Polymorphism  

---

## 🏗️ Features
- **Device (Parent Class):**
  - Stores brand and model.
  - Provides basic device information.

- **Smartphone (Child Class):**
  - Inherits from `Device`.
  - Adds `storage` and private `__battery` attributes.
  - Methods to simulate phone usage (`use`) and get battery status.
  - Overrides `device_info` to show extended details.

---

## 🔑 Code Example

```python
# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.__battery = battery   # encapsulation

    def use(self, hours):
        self.__battery -= hours * 5
        if self.__battery <= 0:
            self.__battery = 0
            return "Battery drained! 🔋"
        return f"Battery at {self.__battery}%"

    def get_battery(self):
        return f"{self.__battery}% remaining"

    def device_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 100)
phone2 = Smartphone("Apple", "iPhone 15", 512, 80)

print(phone1.device_info())   # Samsung Galaxy S24 | Storage: 256GB
print(phone1.use(10))         # Battery at 50%
print(phone1.get_battery())   # 50% remaining

print(phone2.device_info())   # Apple iPhone 15 | Storage: 512GB
print(phone2.use(20))         # Battery drained! 🔋
print(phone2.get_battery())   # 0% remaining
```

---

## 🚀 How to Run
1. Copy the code into a file called `smartphone.py`.
2. Run it with:
   ```bash
   main.py
   ```
3. You’ll see how inheritance, encapsulation, and polymorphism work in action.

---

## 🎯 OOP Concepts Demonstrated
- **Encapsulation** → Battery is private (`__battery`) and accessed through a getter.  
- **Inheritance** → `Smartphone` inherits from `Device`.  
- **Polymorphism** → `device_info` is overridden in `Smartphone`.  

---

## 📊 UML Diagram
```
Device (Parent)
    └── Smartphone (Child)

+ Device
  - brand
  - model
  + device_info()

+ Smartphone(Device)
  - storage
  - __battery (private)
  + use(hours)
  + get_battery()
  + device_info() [overridden]
```

---

## 👨‍💻 Author
Created by **Ogada Brian** as part of a Python OOP assignment.
