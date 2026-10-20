
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



# Creating Plant objects

plant1 = Plant("Basil", "Herb", 1.5)
plant2 = Plant ("Rose", "Shrub", 3)

# Accessing instance variables directly

print (f"Plant 1 - Plant Name: {plant1.name}, Plant type : {plant1.plant_type}, Plant height:  {plant1.height}")
print (f"Plant 2 - Plant Name: {plant2.name}, Plant type : {plant2.plant_type}, Plant height:  {plant2.height}")

# Accessing the class variable
print (f"Total Plant in my collection: {Plant.total_plants}")

# Calling the instance method
plant1.display_plant()
plant2.display_plant()