
# ===========================
# Part B - Plant OOP Project
# ===========================

# ===========================
# Parent Class - Plant
# ===========================

class Plant: 
    total_plants = 0    # Class variable 

    # Constructor and instance variables
    def __init__(self, name, plant_type, height): 
        self.name = name
        self.plant_type = plant_type 
        self.height = height 

        Plant.total_plants += 1

    # Instance method - Display plant information 

    def display_plant(self): 
        print (f"Plant Name: {self.name}, Plant Type: {self.plant_type}, Height: {self.height} feet")

    # Class method - Display total number of plants 
    @classmethod 
    def show_total_plants(cls): 
        print(f"Total Plants in my collection: {cls.total_plants}")

    # Static method - Check whether a height is positive 
    @staticmethod
    def is_valid_height(height): 
        if height > 0: 
            return True
        else: 
            return False 

# Child Class - Herb (Single Inheritance)
class Herb(Plant): 

    # Constructor for Herb 
    def __init__(self, name, height): 
        super().__init__(name, "Herb", height)

    # Instance method - Check herb height 
    def check_height(self): 
        if self.height <=3: 
            print (f"{self.name} is within the 3-foot herb height limit.")
        else: 
            print (f"{self.name} exceeds the 3-foot herb height limit.") 

# =====================================
# Creating Plant objects
# =====================================

plant1 = Plant ("Rose", "Shrub", 3)
plant2 = Plant("Mango", "Tree", 12)


# Calling the instance method
plant1.display_plant()
plant2.display_plant()



# =====================================
# Creating Herb objects
# =====================================

herb1 = Herb ("Basil", 1.5)
herb2 = Herb("Mint", 4)

# Calling the inherited instance method from Plant
herb1.display_plant()
herb2.display_plant()

# Calling the Herb class instance method
herb1.check_height()
herb2.check_height()

# =====================================
# Calling the class method
# =====================================

Plant.show_total_plants()

# =====================================
# Calling the static method
# =====================================

print(f"Is 2 feet a valid height? {Plant.is_valid_height(2)}")
print(f"Is -1 foot a valid height? {Plant.is_valid_height(-1)}")

# Accessing instance variables directly

print (f"Plant 1 - Plant Name: {plant1.name}, Plant type : {plant1.plant_type}, Plant height:  {plant1.height}")
print (f"Plant 2 - Plant Name: {plant2.name}, Plant type : {plant2.plant_type}, Plant height:  {plant2.height}")



