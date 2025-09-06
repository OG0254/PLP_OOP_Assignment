# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # call the parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.__battery = battery   # encapsulation (private attribute)

    # Method to simulate using the phone
    def use(self, hours):
        self.__battery -= hours * 5
        if self.__battery <= 0:
            self.__battery = 0
            return "Battery drained! 🔋"
        return f"Battery at {self.__battery}%"

    # Getter for battery (controlled access)
    def get_battery(self):
        return f"{self.__battery}% remaining"

    # Polymorphism (override device_info)
    def device_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB"


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 100)
phone2 = Smartphone("Apple", "iPhone 15", 512, 80)

print(phone1.device_info())  # Samsung Galaxy S24 | Storage: 256GB
print(phone1.use(10))        # Battery at 50%
print(phone1.get_battery())  # 50% remaining

print(phone2.device_info())  # Apple iPhone 15 | Storage: 512GB
print(phone2.use(20))        # Battery drained! 🔋
print(phone2.get_battery())  # 0% remaining
