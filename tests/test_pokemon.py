import unittest
from code import pokemon


class TestSnakes(unittest.TestCase):
    def test_pokemon_can_deal_damage(self):
        pikachu = {
            'health': 100,
            'power': 50,
            'name': 'Pikachu'
        }

        butterfree = {
            'health': 50,
            'power': 40,
            'name': 'Butterfree'
        }

        result = pokemon.attack(pikachu, butterfree)
        self.assertEqual(result, 'Pikachu hits Butterfree for 50!')


if __name__ == '__main__':
    unittest.main()
