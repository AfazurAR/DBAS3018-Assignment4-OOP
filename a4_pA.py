
# =====================
# defining the class 
# =====================

class Car:
# defining the function with __init__ method 
    def __init__(self, make, model , year):
        self.make = make 
        self.model = model 
        self. year = year

    def display_info(self):          
        print(f"Car information: Make: {self.make}, Model: {self.model}, Year: {self.year}")

Car1 = Car("Toyota", "Corolla", 2020)
Car2 = Car("Honda", "Civic", 2021)

# print (Car1.make, Car1.model, Car1.year)
# print (Car1) 
Car1.display_info()
Car2.display_info()

# ===================== 
# Inheritance 
# =====================

class ElectricCar(Car): 
    def __init__(self, make, model, year, battery_size): 
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"First Electric Car's  Battery information: {self.battery_size} kwh")

eCar1 = ElectricCar("Hyundai","Sonata", 2024, 30)

# To display all elements of Electrict Car1

eCar1.display_info() 

# To display only the Battery Size

print(f"First Electric Car's Battery size is: {eCar1.battery_size}") 

# To call battery information 

eCar1.describe_battery()
