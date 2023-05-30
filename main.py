import requests
import random

starter = input("welcome to the pokemon suggestion program enter start to recieve a pokemon suggestion:")

numb = random.randint(1,1015)
URL = "https://pokeapi.co/api/v2/pokemon/" + str(numb)

response = requests.get(URL) # Get data from the URL

response.raise_for_status()  # Throw an exception if the request failed

data = response.json()

if starter == "start":
  print("you should go find a shiny " + data["name"])
  abilities = [ability["ability"]["name"] for ability in data["abilities"]]
  print("Here are the abilities:")
  for ability in abilities:
    print(ability)
else:
  starter=input("Please type in start to get a pokemon: ")