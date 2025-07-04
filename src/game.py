'''
Pokemon The North Edition 
Print something on the screen 
Introduction -> Welcome to Pokemon The North Edition
Message: Please select pokemon -> list pokemon -> type to choose one (pick by numbers 1-7)
You can make all the pokemon the same if you want to but the user has to pick 
Class: *
Keep hit points and attack damage secret
Alternate to pick pokemon for belt:
Player one pick your pokemon
Player two pick your pokemon 

Pick pokemon for battle (must not have fainted):
Start Battle !!!!
Import Time 
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

Game ends if one player has 3 fainted pokemon
Do you wanna restart or exit 
Restart

'''
import time
import os
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
    Quilava = Fire('Quilava', 58, 22, 'Eruption')
    Meowth = Normal('Meowth', 48, 15, 'Growl')
    Poliwhirl = Water('Poliwhirl', 65, 20, 'Hydro vortex')
    Meganium = Grass('Meganium', 80, 28, 'G-Max drum solo')
    Cyndaquil  = Fire('Cyndaquil', 46, 16, 'Flame charge')
    Blastoise = Water('Blastoise', 79, 30, 'Wave crash')
    Septile = Grass('Septile', 70, 25,'Apple acid')
    pokelist = [Flareon,Eevee,Vaporeon,Leafeon,Charmander,Squirtle,
    Bulbasaur,Quilava,Meowth,Poliwhirl,Meganium,Cyndaquil,Blastoise,Septile]
    Player1 = Trainer()
    Player2 = Trainer()
    
    print("Welcome to Pokemon The North Edition")

    time.sleep(2)

    print("Here are your Pokemon: ")
    time.sleep(1)
    for i, poke in enumerate(pokelist):
        print(f"{i+1}: ", poke.name)
    player_selection = [[],[]]
    for i in range(6):
            not_picked = True
            while not_picked or choice >= 15 or choice <= 0:
                try:
                    choice = int(input(f'Player1 pick Pokemon number {i+1} for your belt:'))

                    # if any(any(choice)):
                    is_match = False
                    for list in player_selection:
                        for element in list:
                            if choice == element:
                                print("Please pick another pokemon")
                                is_match = True
                    if is_match: 
                         continue            
                    not_picked = False
                except (ValueError,TypeError):
                    print("Please enter a number!")
                    continue
                if choice >= 15 or choice <= 0:
                     print("Please pick a number from 1 - 14!")
            player_selection[0].append(choice)
            not_picked = True
            while not_picked or not_picked or choice >= 15 or choice <= 0:
                try:
                    choice = int(input(f'Player2 pick Pokemon number {i+1} for your belt:'))
                    is_match = False
                    for list in player_selection:
                        for element in list:
                            if choice == element:
                                print("Please pick another pokemon")
                                is_match = True
                    if is_match:
                         continue
                    not_picked = False
                except (ValueError,TypeError):
                    print("Please enter a number!")
                    continue
                if choice >= 15 or choice <= 0:
                     print("Please pick a number from 1 - 14!")
            player_selection[1].append(choice)

    for i in player_selection[0]:
         Player1.throw_pokeball(pokelist[i - 1])

    for i in player_selection[1]:
        Player2.throw_pokeball(pokelist[i - 1])

    Endgame = False
    
    while Endgame == False:
        battle_belt1 = {}
        battle_belt2 = {}
        for key, poke in enumerate(Player1.belt):
            battle_belt1[key + 1] = poke.pokemon.name

        print("Player 1: ", battle_belt1)

        for key, poke in enumerate(Player2.belt):
            battle_belt2[key + 1] = poke.pokemon.name

        print("Player 2: ", battle_belt2)

        pokemon_selected = 0
        pokemon1 = 0
        pokemon2 = 0
        first_go1 = True
        first_go2 = True
        while pokemon_selected == 0 or pokemon1 <= 0 or pokemon1 >= 7:
            try:
                pokemon1 = int(input("Player 1 please choose your pokemon (type 1 - 6): "))
                pokemon_selected = 1
                
            except (ValueError,TypeError):
                print("Please enter a number!")
                continue

            if pokemon2 <= 0 or pokemon2 >= 7:
                print("Please pick a number from 1 - 6!")
            
        print(f"You have selected: {Player1.belt[pokemon1 - 1].pokemon.name}")
        
        while pokemon_selected == 0 or pokemon2 <= 0 or pokemon2 >= 7:
            try:
                pokemon2 = int(input("Player 2 choose your pokemon (type 1 - 6): "))
            except (ValueError,TypeError):
                    print("Please enter a number!")
                    continue

            if pokemon2 <= 0 or pokemon2 >= 7:
                print("Please pick a number from 1 - 6:")

                
        print(f"You have selected: {Player2.belt[pokemon2 - 1].pokemon.name}")

        pokemon1 = Player1.belt[pokemon1 - 1].pokemon

        pokemon2 = Player2.belt[pokemon2 - 1].pokemon

        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
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
        count1 = 0
        for poke in Player1.belt:
            if poke.pokemon.has_fainted():
                count1 += 1
        
        count2 = 0
        for poke in Player2.belt:
            if poke.pokemon.has_fainted():
                count2 += 1

        if count1 == 6 or count2 == 6:
            if count1 < count2:
                print("Player 1 is the Winner !!!!!!")
            if count1 > count2:
                print("Player 2 is the Winner !!!!!!")
            
            Endgame = True

            
    try:
        player_input = int(input("Enter 1 to restart or anything else to exit: "))
        time.sleep(2)
    except (TypeError,ValueError):
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    


print("GAME OVER")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')






