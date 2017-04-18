import unittest
from code import something


class TestSomething(unittest.TestCase):
    def test_what_am_i_doing(self):
        self.assertEqual(something.foo(), 7)

    def test_using_variables(self):
        self.assertEqual(something.y, 7)

    # def testing_titles(self):
    #     boy_name = raw_input('What is boy name? ')
    #     girl_name = raw_input('What is girl name? ')
    #     self.assertEqual(boy_name, girl_name)

    def test_math(self):
        result = something.add5(4)
        self.assertEqual(result, 9)

        result2 = something.add5(7)
        self.assertEqual(result2, 12)

        result3 = something.add5(10)
        self.assertEqual(result3, 15)

    def test_math2(self):
        expression = something.get_remainder(5)
        self.assertEqual(expression, 1)

        expression2 = something.get_remainder(8)
        self.assertEqual(expression2, 0)

        expression3 = something.get_remainder(9)
        self.assertEqual(expression3, 1)

    def test_gender(self):
        gender1 = something.get_gender('x', 'x')
        self.assertEqual(gender1, 'female')

        gender2 = something.get_gender('x', 'y')
        self.assertEqual(gender2, 'male')

        gender3 = something.get_gender('y', 'x')
        self.assertEqual(gender3, 'male')

        gender4 = something.get_gender('y', 'y')
        self.assertEqual(gender4, 'invalid')


if __name__ == '__main__':
    unittest.main()
