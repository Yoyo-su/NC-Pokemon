import pytest
from src.pokemon import *

#### TESTS ####
class TestPoke:
    @pytest.mark.it('should create a pokemon with the given attributes')
    def test_pokemon_creates_a_pokemon(self):
        Eevee = Pokemon('Eevee', 55, 18, 'Headbutt')
        assert Eevee.name == 'Eevee'
        assert Eevee.hit_points == 55
        assert Eevee.attack_damage == 18
        assert Eevee.move == 'Headbutt'
class TestUseMove:
    @pytest.mark.it('should return a string with the given pokemons move')
    def test_use_move_returns_string(self):
        Eevee = Pokemon('Eevee', 55, 18, 'Headbutt')
        assert Eevee.use_move() == 'Eevee used Headbutt'
class TestTakeDamage:
    @pytest.mark.it('should take a number and reduce hit points (health) by that number')
    def test_take_damage_reduces_hitpoints_by_given_number(self):
        Eevee = Pokemon('Eevee', 55, 18, 'Headbutt')
        Eevee.take_damage(10)
        assert Eevee.hit_points == 45
class TestHasFainted:
    @pytest.mark.it('should return true if pokemon has zero hitpoints')
    def test_has_fainted_returns_true_if_zero_hitpoints(self):
        Eevee = Pokemon('Eevee', 55, 18, 'Headbutt')
        Eevee.take_damage(55)
        assert Eevee.has_fainted() is True
    @pytest.mark.it('should return false if pokemon has hitpoints left')
    def test_has_fainted_returns_false_if_has_hitpoints(self):
        Eevee = Pokemon('Eevee', 55, 18, 'Headbutt')
        Eevee.take_damage(10)
        assert Eevee.has_fainted() is False
class TestType:
    @pytest.mark.it('should create a pokemon with the given type')
    def test_type_creates_a_pokemon_with_type(self):
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        assert Eevee.type == 'normal'
    @pytest.mark.it('fire should be strong against grass')
    def test_strong_against_grass_if_fire(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        assert Flareon.strong_against == 'grass'
    @pytest.mark.it('fire should be weak against water')
    def test_weak_against_water_if_fire(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        assert Flareon.weak_against == 'water'
class TestGetMultiplier:
    @pytest.mark.it('should return 1.5 if stronger than given pokemon')
    def test_get_multiplier_returns_if_stronger(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Leafeon = Grass('Leafeon', 65, 17, 'Giga drain')
        assert Flareon.get_multiplier(Leafeon) == 1.5
    @pytest.mark.it('should return 0.5 if weakeer than given pokemon')
    def test_get_multiplier_returns_if_weaker(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        assert Flareon.get_multiplier(Vaporeon) == 0.5
    @pytest.mark.it('should return 1 if neither stronger or weaker than given pokemon')
    def test_get_multiplier_returns_if_normal(self):
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        assert Eevee.get_multiplier(Vaporeon) == 1

class TestPokeball:
    @pytest.mark.it('should return None when checking self.pokemon property')
    def test_pokemon_property(self):
        test_pokeball = Pokeball()
        assert test_pokeball.pokemon == None

    @pytest.mark.it('should return pokemon when using the catch method')
    def test_catch_method(self):
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        test_pokeball = Pokeball()
        test_pokeball.catch(Eevee)
        assert test_pokeball.pokemon == Eevee

    @pytest.mark.it('should return True when using is_empty and pokeball has no pokemon')
    def test_is_empty(self):
        test_pokeball = Pokeball()
        assert test_pokeball.is_empty() == True

    @pytest.mark.it('should return False when using is_empty and pokeball has a pokemon')
    def test_is_empty_false(self):
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        test_pokeball = Pokeball()
        test_pokeball.catch(Eevee)
        assert test_pokeball.is_empty() == False


class TestTrainer:
    @pytest.mark.it('should return 6 pokeballs in the belt')
    def test_belt(self):
        test_trainer = Trainer()
        assert test_trainer.belt == [test_trainer.ball1, test_trainer.ball2, test_trainer.ball3, test_trainer.ball4, test_trainer.ball5, test_trainer.ball6]


    @pytest.mark.it('should return the pokemon added to Pokeball one')
    def test_catch(self):
        test_trainer = Trainer()
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        test_trainer.throw_pokeball(Flareon)
        assert test_trainer.ball1.pokemon == Flareon

    @pytest.mark.it('should return the pokemon added to Pokeball one')
    def test_catch_2(self):
        test_trainer = Trainer()
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        test_trainer.throw_pokeball(Flareon)
        test_trainer.throw_pokeball(Eevee)
        assert test_trainer.ball2.pokemon == Eevee

    @pytest.mark.it('should return only 6 pokeballs when given more')
    def test_catch_6_or_more(self):
        test_trainer = Trainer()
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Eevee = Normal('Eevee', 55, 18, 'Headbutt')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        Leafeon = Grass('Leafeon', 65, 17, 'Giga drain')
        Charmander = Fire('Charmander', 44, 17, 'Flamethrower')
        Squirtle = Water('Squirtle', 44, 16, 'Surf')
        Bulbasaur = Grass('Bulbasaur', 45, 16,'Razor leaf')
        test_trainer.throw_pokeball(Flareon)
        test_trainer.throw_pokeball(Eevee)
        test_trainer.throw_pokeball(Vaporeon)
        test_trainer.throw_pokeball(Leafeon)
        test_trainer.throw_pokeball(Charmander)
        test_trainer.throw_pokeball(Squirtle)
        test_trainer.throw_pokeball(Bulbasaur)
        assert test_trainer.ball6.pokemon == Squirtle
        assert len(test_trainer.belt) == 6

class TestBattle:
    @pytest.mark.it('should return pokemon 2 with less hitpoints according to Pokemon methods')
    def test_battle(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_battle = Battle(Flareon, Vaporeon)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 60

    @pytest.mark.it('should return true when pokemon faints after a long battle')
    def test_battle_turn_2(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_battle = Battle(Flareon, Vaporeon)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 60
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (19 * 1.5)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 50
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (2 * (19 * 1.5))
        test_battle.take_turn()
        assert Vaporeon.hit_points == 40
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (3 * (19 * 1.5))
        test_battle.take_turn()
        assert Flareon.has_fainted() == True

    @pytest.mark.it('should return the winning pokemon after a long battle')
    def test_battle_winner(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_battle = Battle(Flareon, Vaporeon)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 60
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (19 * 1.5)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 50
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (2 * (19 * 1.5))
        test_battle.take_turn()
        assert Vaporeon.hit_points == 40
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (3 * (19 * 1.5))
        test_battle.take_turn()
        assert test_battle.get_winner() == test_battle.pokemon2

    @pytest.mark.it('should return None when neither pokemon has fainted during a battle')
    def test_battle_winner_none(self):
        Flareon = Fire('Flareon', 65, 20, 'Fire blast')
        Vaporeon = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_battle = Battle(Flareon, Vaporeon)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 60
        test_battle.take_turn()
        assert Flareon.hit_points == 65 - (19 * 1.5)
        test_battle.take_turn()
        assert Vaporeon.hit_points == 50
        assert test_battle.get_winner() == None






    





        

    
    