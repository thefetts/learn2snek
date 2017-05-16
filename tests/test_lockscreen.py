import unittest

from code import lockscreen


class TestLockscreen(unittest.TestCase):
    def test_a_1x1_screen(self):
        # result = lockscreen.permutations(1, 1, 1)
        result = lockscreen.permutations(1)
        self.assertEqual(result, 1)

    def test_a_2x2_screen(self):
        # result = lockscreen.permutations(2, 2, 1)
        result = lockscreen.permutations(2)
        self.assertEqual(result, 28)

        # result = lockscreen.permutations(2, 2, 2)
        # self.assertEqual(result, 24)
        #
        # result = lockscreen.permutations(2, 2, 3)
        # self.assertEqual(result, 16)
        #
        # result = lockscreen.permutations(2, 2, 4)
        # self.assertEqual(result, 8)

    # def test_a_1x2_screen(self):
    #     result = lockscreen.permutations(1, 2, 1)
    #     self.assertEqual(result, 4)
    #
    #     result = lockscreen.permutations(1, 2, 2)
    #     self.assertEqual(result, 2)

    # def test_rotation_has_no_effect(self):
    #     result1 = lockscreen.permutations(2, 4, 2)
    #     result2 = lockscreen.permutations(4, 2, 2)
    #     self.assertEqual(result1, result2)

    # def test_invalid_min(self):
    #     result = lockscreen.permutations(3, 2, 9)
    #     self.assertEqual(result, '9 is an invalid minimum, we only have 6 dots to work with!')
    #
    #     result = lockscreen.permutations(33, 7, 5000)
    #     self.assertEqual(result, '5000 is an invalid minimum, we only have 231 dots to work with!')


if __name__ == '__main__':
    unittest.main()
