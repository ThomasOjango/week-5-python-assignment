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
        super().__init__(brand, model)  # Inheriting from Device
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"Calling {number}  from {self.device_info()}"

    def charge(self, percent):
        self.battery += percent
        return f"{self.device_info()} charged to {self.battery}% "

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 50)
phone2 = Smartphone("Apple", "iPhone 15", "512GB", 80)

# Using methods
print(phone1.make_call("0759678286"))
print(phone1.charge(20))
print(phone2.device_info())
