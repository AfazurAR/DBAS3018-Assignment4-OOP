# defining the class 
class Cars:
# defining the function with __init__ method 
    def __init__(self, make, model , year):
        self.make = make 
        self.model = model 
        self. year = year

    def display_info (self):          
        return f"{self.make} {self.model} {self.year}"

Car1 = Cars("Toyota", "Corolla", 2020)
cart2 = Cars("Honda", "Civic", 2021)

# print (Car1.make, Car1.model, Car1.year)
# print (Car1) 
print (Car1.display_info())
print (cart2.display_info())

