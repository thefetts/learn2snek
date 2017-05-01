import unittest
from code import q1


class TestQ1(unittest.TestCase):
    # def test_q1(self):
    # self.assertEqual(droprates.grams("anagram", "nag a zam"), "bropen!!")
    # self.assertEqual(q1.assessment(), 7)



    def test_words(self):
        one_sentence = "this is a sentence."
        same_word_sentence = "this this this is me me me"
        single_word_sentences = "One. Two? Three! Three?"
        three_sentences = "this is a sentence. This is also a sentence; do i need to count numbers (4) as words?"
        number_sentence = "this is a sentence with numbers in it; 1, 2, 3, and 4."
        self.assertEqual(q1.word_count(one_sentence), "Total word count: 4")
        self.assertEqual(q1.word_count(three_sentences), "Total word count: 18")
        self.assertEqual(q1.word_count(number_sentence), "Total word count: 13")
        self.assertEqual(q1.unique_word(same_word_sentence), "Unique words: 3")
        self.assertEqual(q1.unique_word(three_sentences), "Unique words: 15")
        self.assertEqual(q1.sentence_count(one_sentence), "Sentences: 1")
        self.assertEqual(q1.sentence_count(three_sentences), "Sentences: 3")
        self.assertEqual(q1.sentence_count(single_word_sentences), "Sentences: 4")
        self.assertEqual(q1.unique_word(single_word_sentences), "Unique words: 3")


if __name__ == '__main__':
    unittest.main()
