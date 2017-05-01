import unittest
from code import anagrams


class TestAnagrams(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagrams.grams("anagram", "nag a ram"), "is anagram!")
        self.assertEqual(anagrams.grams("anagram", "nag a zam"), "bropen!!")


if __name__ == '__main__':
    unittest.main()
