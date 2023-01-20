import requests

token = 'токен из телеграма'
photo = 'https://i.pinimg.com/originals/80/12/9b/80129b3b19561652c181d2dcb16a0af6.png'

# response = requests.post('https://pokemonbattle.me:5000/trainers/reg', json = {
#     "trainer_token": token,
#     "email": "go13od@yandex.ru",
#     "password": "Iloveqa1"
# }, headers = {'Content-Type': 'application/json'})
# print(response.text)

# response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', json = {
#     "trainer_token": token
# }, headers = {'Content-Type': 'application/json'})
# print(response_confirm.text)

# response_post_pokemons = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
#     "name": "Poke",
#     "photo": photo,
# }, headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_post_pokemons.text)

# pokemon_id = response_post_pokemons.json()['id']

# response_put_pokemons = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
#     "pokemon_id": 3160,
#     "name": "Uha",
#     "photo": photo
# }, headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_put_pokemons.text)

# response_add_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
# json = {"pokemon_id": 3160},
# headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_add_pokeball.text)

# response_change_avatar = requests.post('https://pokemonbattle.me:5000/trainers/change_avatar',
# json = {
#     "card_number": "4620869113632996",
#     "card_csv": "125",
#     "card_actual": "10/25",
# 	"num": "56456",
# 	"avatar_id": "7"
# },
# headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_change_avatar.text)

# response_delete_pokeball = requests.put('https://pokemonbattle.me:5000/trainers/delete_pokeball',
# json = {"pokemon_id": pokemon_id},
# headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_delete_pokeball.text)

# response_battle = requests.post('https://pokemonbattle.me:5000/battle',
# json = {
#     "attacking_pokemon": "3160",
#     "defending_pokemon": "3047"
# },
# headers = {'Content-Type': 'application/json', "trainer_token": token})
# print(response_battle.text)

