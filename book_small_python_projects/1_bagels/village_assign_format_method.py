import random 

# List of Locations
locations = ["Banjul", "Serekunda", "Brikama", "Bakau", "Farafenni"]

# Get user input 
name = input("Nangadef! What is your name? ")

# Randomly assign a village 
assigned_village = random.choice(locations)

# Create message using .format()
message = "Hello {}, you have been assigned to the {} Post.".format(name, assigned_village)

# Print the message
print(message)