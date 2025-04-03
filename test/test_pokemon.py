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