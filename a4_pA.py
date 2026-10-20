
# =====================
# defining the class 
# =====================

class Car:
# defining the function with __init__ method 
    def __init__(self, make, model , year):
        self.make = make 
        self.model = model 
        self. year = year

        self.__mileage = 0 # Encapsulating mileage. 


    def display_info(self):          
        print(f"Car information: Make: {self.make}, Model: {self.model}, Year: {self.year}")


# ===================== 
# Encapsulation
# =====================


    def get_mileage(self): 
        return self.__mileage

    def set_mileage (self, new_mileage): 
        if new_mileage > 0: 
            self.__mileage = new_mileage

# ======================

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


# Accessing Encapsulated information and change it. 

print (f"Car 1 make: {Car1.make}, Getting initial mileage: {Car1.get_mileage()}")
Car1.set_mileage(10)
print (f"Car 1 make: {Car1.make}, Getting new mileage after positive input: {Car1.get_mileage()}")


print (f"Car 1 make: {Car1.make}, Getting initial mileage: {Car1.get_mileage()}")
Car1.set_mileage(-100)
print (f"Car 1 make: {Car1.make}, Getting new mileage after negative input: {Car1.get_mileage()}")


# ===================== 
# Polymorphism
# =====================

# Defining parent class 
class Shape: 
    def area(self): 
        pass 

# Defining child class 
class Circle (Shape): 
    def __init__ (self, radius): 
        self.radius = radius
     

    def area (self): 
        print (3.14*self.radius * self.radius)


c1 = Circle(5)

c1.area()

class Rectangle (Shape):
    def __init__ (self, height, width): 
        self.height = height 
        self.width = width 

    def area (self): 
        print (self.height * self.width)

r1 = Rectangle (5, 2)

r1.area()


# =====================
# Object Interaction
# =====================

class Book: 
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

    def display_book(self):          
        print(f"Book information: Title: {self.title}, Author: {self.author}")

book1 = Book("Lord of the Rings", "Tolkien")
book2 = Book("The Vinchi Code", "Dan Brown")

book1.display_book()
book2.display_book()