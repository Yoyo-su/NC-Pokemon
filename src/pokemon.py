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
        if self.strong_against is other_pokemon.type:
            return 1.5
        if self.weak_against is other_pokemon.type:
            return 0.5
        return 1
    

    
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


    
# test_trainer = Trainer()
# Flareon = Fire('Flareon', 65, 20, 'Fire blast')
# test_trainer.throw_pokeball(Flareon)
# print(Flareon)

#test = Fire()