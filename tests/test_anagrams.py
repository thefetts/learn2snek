import unittest
from code import anagrams


class TestAnagrams(unittest.TestCase):
     def test_anagram(self):
         self.assertEqual(anagrams.grams("anagram", "nag a ram"), "is anagram!")
         self.assertEqual(anagrams.refactor_grams("anagram", "nag a ram"), True)
         self.assertEqual(anagrams.refactor_grams("1234", "2 3 4 1"), True)
         self.assertEqual(anagrams.refactor_grams("hfjdshajfk", "fdjask"), False)
         self.assertEqual(anagrams.add_ten([1,2,3]), [11,12,13])
         self.assertEqual(anagrams.len_words(['great', 'job', 'so', 'far']), [5,3,2,3])
         self.assertEqual(anagrams.letter_counter('words to test', 'aeiou'), {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})
         self.assertEqual(anagrams.remove_item([1,2,3,4,5], 4), [1,2,3,5])
         self.assertEqual(anagrams.cipher('defend the east wall of the castle', dict(zip('abcdefghijklmnopqrstuvwxyz','phqgiumeaylnofdxjkrcvstzwb')),
                                          "encipher"), 'giuifg cei iprc tpnn du cei qprcni')
         self.assertEqual(anagrams.count_isograms(['conduct', 'letter', 'contract', 'enc', 'hours', 'interview']), 2)
         self.assertEqual(anagrams.matching_pairs([('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f',6)]), [(0,4), (1,2), (3,5)])


if __name__ == '__main__':
    unittest.main()
