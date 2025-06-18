import random


"""This is the base class for all Pokemon. The Pokemon class also has methods 
to use a move, take damage, check if it has fainted, and get the multiplier for 
damage based on the type of the Pokemon.
"""
class Pokemon:
    
    def __init__(self, name, hitpoints, attackdamage, move):
        self.name = name
        self.hit_points = hitpoints
        self.attack_damage = attackdamage
        self.move = move

    def use_move(self):
        return f'{self.name} used {self.move}'
    
    def take_damage(self, damage):
        if self.hit_points > 0:
            self.hit_points -= damage

    def has_fainted(self):
        if self.hit_points <= 0:
            return True
        return False
    
    def get_multiplier(self,other_pokemon): 
        def critical_hit():
            dice_roll = random.randint(1,6)
            if dice_roll == 6:
                return True
            return False
        critical = critical_hit()
        if critical:
            print(f"{self.name} got CRITICAL HIT!!!")
            return 3
        if self.strong_against is other_pokemon.type:
            return 1.5
        if self.weak_against is other_pokemon.type:
            return 0.5
        return 1
    
   
    
"""The following classes inherit from the Pokemon class and represent different types of Pokemon"""
class Fire(Pokemon):
    def __init__(self, name, hitpoints, attackdamage, move):
        super().__init__(name, hitpoints, attackdamage, move)
        self.type = 'fire'
        self.strong_against = 'grass'
        self.weak_against = 'water'
    pass
    
class Water(Pokemon):
    def __init__(self, name, hitpoints, attackdamage, move):
        super().__init__(name, hitpoints, attackdamage, move)
        self.type = 'water'
        self.strong_against = 'fire'
        self.weak_against = 'grass'
    pass
class Grass(Pokemon):
    def __init__(self, name, hitpoints, attackdamage, move):
        super().__init__(name, hitpoints, attackdamage, move)
        self.type = 'grass'
        self.strong_against = 'water'
        self.weak_against = 'fire'
    pass
class Normal(Pokemon):
    def __init__(self, name, hitpoints, attackdamage, move):
        super().__init__(name, hitpoints, attackdamage, move)
        self.type = 'normal'
        self.strong_against = None
        self.weak_against = None
    pass

"""The Pokeball class represents a Pokeball that can catch a Pokemon"""
class Pokeball:
    def __init__(self):
        self.pokemon = None

    def catch(self, Pokemon):
        if self.pokemon == None:
            self.pokemon = Pokemon

    def is_empty(self):
        if self.pokemon == None:
            return True
        return False

"""The Trainer class represents a Pokemon Trainer who can throw Pokeballs to catch Pokemon"""
class Trainer:
    def __init__(self):
        self.ball1 = Pokeball()
        self.ball2 = Pokeball()
        self.ball3 = Pokeball()
        self.ball4 = Pokeball()
        self.ball5 = Pokeball()
        self.ball6 = Pokeball()
        self.belt = [self.ball1, self.ball2, self.ball3, self.ball4, self.ball5, self.ball6]

    def throw_pokeball(self, pokemon):
        for pokeball in self.belt:
            if pokeball.is_empty():
                pokeball.catch(pokemon)
                break

"""The Battle class represents a battle between two Pokemon, managing turns and 
determining the winner."""
class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turn = False

    def take_turn(self):
        if not self.pokemon1.has_fainted() and not self.pokemon2.has_fainted():
            if self.turn is False:
                damage = self.pokemon1.attack_damage * self.pokemon1.get_multiplier(self.pokemon2)
                self.pokemon2.take_damage(damage)
                self.turn = not self.turn

            else:
                damage = self.pokemon2.attack_damage * self.pokemon2.get_multiplier(self.pokemon1)
                self.pokemon1.take_damage(damage)
                self.turn = not self.turn
            
    def get_winner(self):
        if self.pokemon1.has_fainted():
                return self.pokemon2

        if self.pokemon2.has_fainted():
                return self.pokemon1

        return None
     
     
     
