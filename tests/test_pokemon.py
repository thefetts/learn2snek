import unittest

from code import pokemon


class TestSnakes(unittest.TestCase):
    def test_pokemon_can_deal_damage(self):
        result = pokemon.attack('Pikachu', 'Butterfree')
        self.assertEqual(result, [
            'Pikachu hits Butterfree for 50!',
            'Butterfree has 10 HP remaining.'
        ])

    def test_pokemon_can_faint(self):
        result = pokemon.attack('Charizard', 'Butterfree')
        self.assertEqual(result, [
            'Charizard hits Butterfree for 70!',
            'Butterfree has fainted!'
        ])

    def test_pokemon_battle_lists_both_attacks(self):
        result = pokemon.battle('Pikachu', 'Butterfree')
        self.assertEqual(result, [
            'Pikachu hits Butterfree for 50!',
            'Butterfree has 10 HP remaining.',
            'Butterfree hits Pikachu for 40!',
            'Pikachu has 60 HP remaining.',
            'Pikachu hits Butterfree for 50!',
            'Butterfree has fainted!'
        ])
    def test_epic_pokemon(self):
        result = pokemon.battle('Mew','Mewtwo')
        self.assertEqual(result, [
            'Mew hits Mewtwo for 100!',
            'Mewtwo has 400 HP remaining.',
            'Mewtwo hits Mew for 100!',
            'Mew has 400 HP remaining.',
            'Mew hits Mewtwo for 100!',
            'Mewtwo has 300 HP remaining.',
            'Mewtwo hits Mew for 100!',
            'Mew has 300 HP remaining.',
            'Mew hits Mewtwo for 100!',
            'Mewtwo has 200 HP remaining.',
            'Mewtwo hits Mew for 100!',
            'Mew has 200 HP remaining.',
            'Mew hits Mewtwo for 100!',
            'Mewtwo has 100 HP remaining.',
            'Mewtwo hits Mew for 100!',
            'Mew has 100 HP remaining.',
            'Mew hits Mewtwo for 100!',
            'Mewtwo has fainted!'
        ])
def test_sick_pokemon(self):
        result = pokemon.battle('Mew','Oddish')
        self.assertEqual(result, [
            'Oddish has fainted!'
        ])

if __name__ == '__main__':
    unittest.main()
