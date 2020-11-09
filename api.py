import requests
from emoji import emojize

# Receives the status code from the website
response = requests.get("https://www.bbc.co.uk/")

# Code 200 = live -- 404 is error not found

# first iteration
if response.status_code == 200:
    print("Up and running")
elif response.status_code == 404:
    print("Unavailable")
else:
    print("Oops, something went wrong!")

#second iteration
def check_response_code(response):
    if response.status_code == 200:
        print("Up and running")
    elif response.status_code == 404:
        print("Unavailable")
    else:
        print("Oops, something went wrong!")
