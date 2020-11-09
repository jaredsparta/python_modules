import requests
from emoji import emojize

response = requests.get("https://www.bbc.co.uk/")

print(emojize(":thumbs_up:"))
print(response)

if response.status_code == 200:
    print("Up and running")
