
# ===========================
# Creating a Parent Class - Plant
# ===========================

class Plant: 
    def __init__(self, name, plant_type, height): 
        self.name = name
        self.plant_type = plant_type 
        self.height = height 

# Creating object 

plant1 = Plant("Basil", "Herb", 1.5)

# Accessing attributes 

print (plant1.name) 
print (plant1.plant_type)
print (plant1.height)
