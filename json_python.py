# Use json module to encode and decode 
import json

# Create a dictionary of a car
car_data = {"name":"Tesla",
            "engine": "Electric battery"}

# Methods:

# json.dumps(<dictionary name>) creates a string object of the dictionary
# Serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(type(car_data_json_string)) # A string

# This block of code will create a new .json file in the folder
# with the name specified in the open() keyword
# This is encoding a dictionary into a write file
with open("car_data.json", "w") as jsonfile:
    json.dump(car_data, jsonfile, indent=4, sort_keys=True)

with open("car_data.json", "r") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])