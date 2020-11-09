import requests
import json

# arguement = input("Please enter your post code: ")
# url_target = live_response + arguement

# How to convert this datatype 'bytes' into dictionary
# HINT: python json library
# Then iterate through the data and print RESULTS
# Print the longitudinal and latitudinal coordinates
# Create a function that returns the longitude and latitude of the given postcode
# Use input to get the given postcode

# print(str(live_response.content))

def get_ll():
    arg = input("Please enter your postcode: ")
    postcode = "http://api.postcodes.io/postcodes/" + arg
    response = requests.get(postcode)
    print(response.status_code)
    if not response.status_code == 200:
        return print("Sorry, not in database")
    val_1 = response.content
    dic = json.loads(val_1)
    print(f"latitude: {dic['result']['latitude']}")
    print(f"longitude: {dic['result']['longitude']}")
    input("\nPress enter to see results")
    for key, value in dic['result'].items():
        print(f"{key} : {value}")

get_ll()
