import requests
import random
import webbrowser

getpokemon = input("Welcome to the Pokémon suggestion program. Enter start to receive a Pokémon suggestion:")
version = input("Enter the name of the game version you prefer (e.g., red, blue, emerald): ")

def get_pokemon_data(pokemon_id, version):
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    params = {'version': version}
    response = requests.get(URL, params=params)  # Get data from the URL with version parameter
    response.raise_for_status()  # Throw an exception if the request failed
    data = response.json()
    return data

def get_pokemon_weaknesses(pokemon_types):
    URL = "https://pokeapi.co/api/v2/type/"
    weaknesses = {}
    for pokemon_type in pokemon_types:
        response = requests.get(URL + pokemon_type)
        response.raise_for_status()
        data = response.json()
        damage_relations = data["damage_relations"]
        for key, value in damage_relations.items():
            if key.startswith("double_damage_to"):
                for weak_type in value:
                    weak_type_name = weak_type["name"]
                    weaknesses[weak_type_name] = weaknesses.get(weak_type_name, 0) + 1
    return weaknesses

if getpokemon == "start":
    numb = random.randint(1, 1015)
    pokemon_data = get_pokemon_data(numb, version)
    name = pokemon_data["name"]
    print("You should go find a " + name.capitalize())

    types = [type_data["type"]["name"] for type_data in pokemon_data["types"]]
    print("Types:", ", ".join(types))

    abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
    print("Here are the abilities:")
    for ability in abilities:
        print(ability)

    weaknesses = get_pokemon_weaknesses(types)
    print("Weaknesses:")
    for weakness, count in weaknesses.items():
        print(f"{weakness}")

    picture_url = pokemon_data["sprites"]["front_default"]
    if picture_url:
        webbrowser.open(picture_url)

else:
    getpokemon = input("Please type in start to find a Pokémon. ")