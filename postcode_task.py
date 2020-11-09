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
    # Asks user to input a postcode
    arg = input("Please enter your postcode: ")
    postcode = "http://api.postcodes.io/postcodes/" + arg

    # This gets the status code from the site
    # If not valid, the function ends
    response = requests.get(postcode)
    print(response.status_code)
    if not response.status_code == 200:
        return print("Sorry, not in database")
   
    # This receives the content from the API
    val_1 = response.content
    # I use json.loads() to turn the bytes into a dictionary
    dic = json.loads(val_1)

    # As required, I print out the latitude and longitude of the postcode
    print(f"latitude: {dic['result']['latitude']}")
    print(f"longitude: {dic['result']['longitude']}")

    # I put this in so people can choose when to see the rest of the results
    input("\nPress enter to see results")
    
    # This prints out the rest of the results that the API returns
    for key, value in dic['result'].items():
        print(f"{key} : {value}")

get_ll()
