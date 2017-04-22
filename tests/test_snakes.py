import unittest
from code import snakes
Snake = snakes.Snake


# Here are a bunch of test cases for finding venomous snakes!
# I haven't solved this, so I might have all sorts of problems with these tests, who knows!
# I commented all of the other tests and assertions out so you can work iteratively
# Get the first assertEqual to pass, then uncomment the next line, making it pass before moving on
# Once a whole test is working, uncomment the next def line and the first assertEqual and carry on!
class TestSnakes(unittest.TestCase):
    def test_is_venomous_finds_coral_snakes(self):
        # Any snake with red touching yellow on either side is deadly
        # Some of these aren't real Coral snake configurations, but that's ok for today :)

        # One example using the Snake class and object-oriented programming
        self.assertEqual(Snake(['red', 'yellow']).is_venomous(), "You're a dead fellow!")

        # The rest of the examples use functional programming
        self.assertEqual(snakes.is_venomous(['black', 'yellow', 'red', 'yellow']), "You're a dead fellow!")
        self.assertEqual(snakes.is_venomous(['black', 'yellow', 'red']), "You're a dead fellow!")

    def test_is_venomous_finds_scarlet_king_snakes(self):
        # Any snake with red touching black on either side is fine
        # Some of these aren't real Scarlet King snake configurations, but that's ok for today :)

        self.assertEqual(snakes.is_venomous(['red', 'black']), "You're ok Jack!")
        self.assertEqual(snakes.is_venomous(['black', 'red', 'black', 'yellow']), "You're ok Jack!")
        self.assertEqual(snakes.is_venomous(['yellow', 'black', 'red']), "You're ok Jack!")

    def test_is_venomous_finds_invalid_snakes(self):
        # Bad snakes are anything that don't fit in the above two rules

        self.assertEqual(snakes.is_venomous(['green', 'red', 'orange', 'black']), "BAD SNEK!")
        self.assertEqual(snakes.is_venomous([]), "BAD SNEK!")
        self.assertEqual(snakes.is_venomous(['RED RED RED RED RED RED JUST A RED SNAKE']), "BAD SNEK!")
        self.assertEqual(snakes.is_venomous(['yellow', 'black', 'yellow', 'black']), "BAD SNEK!")


if __name__ == '__main__':
    unittest.main()
