'''
Pokemon The North Edition 
Print something on the screen 
Introduction -> Welcome to Pokemon The North Edition
Message: Please select pokemon -> list pokemon -> type to choose one (pick by numbers 1-7)
You can make all the pokemon the same if you want to but the user has to pick 
Class: *
Keep hit points and attack damage secret
Player one pick your pokemon
Player two pick your pokemon 
Start Battle !!!!
Import Time 
While Looper.cpu 
delay a couple secs
Show battle turn by turn
f"{pokemon 1} attacks {pokemon 2} with {pokemon 1 move}"
f"pokemon 2 hipoints = {pokemon 2 hitpoints}"

f"{pokemon 2} attacks {pokemon 1} with {pokemon 2 move}"
f"pokemon 1 hipoints = {pokemon 1 hitpoints}"

f"{pokemon 2} has fainted"
f"{pokemon 1} is the winner !!!!!"

Loop runs take_turn method until get_winner is truthy 
Pokemon (pokemon name) is the Winner !!!! 
Time module
Make it more suspensful and show hit points and attack damage until game over 
Do you wanna restart or exit 
Restart

'''
import time
from pokemon import * 

player_input = 1

while player_input == 1:

    Flareon = Fire('Flareon', 65, 20, 'Fire blast')
    Eevee = Normal('Eevee', 55, 18, 'Headbutt')
    Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
    Leafeon = Grass('Leafeon', 65, 17, 'Giga drain')
    Charmander = Fire('Charmander', 44, 17, 'Flamethrower')
    Squirtle = Water('Squirtle', 44, 16, 'Surf')
    Bulbasaur = Grass('Bulbasaur', 45, 16,'Razor leaf')

    pokelist = [Flareon, Eevee, Vaporeon, Leafeon, Charmander, Squirtle, Bulbasaur]
    
    print("Welcome to Pokemon The North Edition")

    time.sleep(2)

    print("Here are your Pokemon: ")
    time.sleep(1)
    print("1: ", Flareon.name)
    print("2: ", Eevee.name)
    print("3: ", Vaporeon.name)
    print("4: ", Leafeon.name)
    print("5: ", Charmander.name)
    print("6: ", Squirtle.name)
    print("7: ", Bulbasaur.name)

    pokemon1 = int(input("Player 1 please choose your pokemon (type 1 - 7): "))
    print(f"You have selected: {pokelist[pokemon1 - 1].name}")

    pokemon2 = int(input("Player 2 choose your pokemon (type 1 - 7): "))

    while pokemon2 == pokemon1:
        print("please pick another pokemon")
        pokemon2 = int(input("Player 2 choose your pokemon: "))

    print(f"You have selected: {pokelist[pokemon2 - 1].name}")

    pokemon1 = pokelist[pokemon1 - 1]

    pokemon2 = pokelist[pokemon2 - 1]

    time.sleep(1)

    print("The battle will now commence !!!!!!")

    game_battle = Battle(pokemon1, pokemon2)

    time.sleep(2)

    while not pokemon1.has_fainted() and not pokemon2.has_fainted():
        game_battle.take_turn()
        print(f"{pokemon1.name} attacks {pokemon2.name} with {pokemon1.move}")
        print(f"{pokemon2.name} hitpoints = {pokemon2.hit_points}")
        time.sleep(2)

        if not pokemon2.has_fainted():
            game_battle.take_turn()
            print(f"{pokemon2.name} attacks {pokemon1.name} with {pokemon2.move}")
            print(f"{pokemon1.name} hitpoints = {pokemon1.hit_points}")
            time.sleep(2)

    if pokemon1.has_fainted():
        loser = pokemon1

    if pokemon2.has_fainted():
        loser = pokemon2

    print(f"Oh no {loser.name} you lose")
    time.sleep(2)
    print(f"{game_battle.get_winner().name} wins !!!!!!")
    time.sleep(2)

    player_input = int(input("Enter 1 to restart or anything else to exit: "))
    time.sleep(2)

print("GAME OVER")






