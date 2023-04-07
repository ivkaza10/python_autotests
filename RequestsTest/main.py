import requests
token = 'b4c6a01147dcdc83846bb70a931d0a98'
url = 'https://pokemonbattle.me:9104/'
#Создание покемона
'''response_add_pokemon = requests.post (f'{url}pokemons', 
    headers = {"trainer_token": token},
    json= {
    "name": "Emperor",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)'''
#изменили имя покемона
'''response_change_name = requests.put (f'{url}pokemons', 
    headers = {"trainer_token": token},
    json= {
    "pokemon_id": "8787",
    "name": "Bvgthfnjh",
    
})
print(response_change_name.text)'''

#положили покемона в покетболл
response_catch_pokemon = requests.post (f'{url}trainers/add_pokeball', 
    headers = {"trainer_token": token},
    json= {
    "pokemon_id": "8787"
})
print(response_catch_pokemon.text)