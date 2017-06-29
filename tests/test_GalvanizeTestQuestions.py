import unittest
from code import GalvanizeTestQuestions


class TestAnagrams(unittest.TestCase):
     def test_gal(self):

         self.assertEqual(GalvanizeTestQuestions.add_ten([1,2,3]), [11,12,13])
         self.assertEqual(GalvanizeTestQuestions.len_words(['great', 'job', 'so', 'far']), [5,3,2,3])
         self.assertEqual(GalvanizeTestQuestions.letter_counter('words to test', 'aeiou'), {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})
         self.assertEqual(GalvanizeTestQuestions.remove_item([1,2,3,4,5], 4), [1,2,3,5])
         self.assertEqual(GalvanizeTestQuestions.cipher('defend the east wall of the castle', dict(zip('abcdefghijklmnopqrstuvwxyz','phqgiumeaylnofdxjkrcvstzwb')),
                                          "encipher"), 'giuifg cei iprc tpnn du cei qprcni')
         self.assertEqual(GalvanizeTestQuestions.count_isograms(['conduct', 'letter', 'contract', 'enc', 'hours', 'interview']), 2)
         self.assertEqual(GalvanizeTestQuestions.matching_pairs([('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f',6)]), [(0,4), (1,2), (3,5)])
         self.assertEqual(GalvanizeTestQuestions.nCr(9,3), 84)
         self.assertEqual(GalvanizeTestQuestions.four_decimals(1.111111), 1.1111)
         self.assertEqual(GalvanizeTestQuestions.binomial_dist(3,0,(1/6)), 0.5787)
         self.assertEqual(GalvanizeTestQuestions.binomial_dist(3,1,(1/6)), 0.3472)
         self.assertEqual(GalvanizeTestQuestions.binomial_dist(10,5,(1/2)), 0.2461)
         self.assertEqual(GalvanizeTestQuestions.binomial_dist(100,20,(1/3)), 0.0013)
         self.assertEqual(GalvanizeTestQuestions.geometric_dist(.30,6), 0.0504)
         self.assertEqual(GalvanizeTestQuestions.geometric_dist(.01,30), 0.0075)
         self.assertEqual(GalvanizeTestQuestions.geometric_dist_sum(.01,52), 0.4111)
         self.assertEqual(GalvanizeTestQuestions.geometric_dist(.68,3), 0.0696)
         self.assertEqual(GalvanizeTestQuestions.poisson_dist(1,.6), .3293)
         self.assertEqual(GalvanizeTestQuestions.poisson_dist(30,40), .0185)
         self.assertEqual(GalvanizeTestQuestions.sample_mean(142, 250), .568)
         self.assertEqual(GalvanizeTestQuestions.sample_variance(142, 250), 0.2464)
         self.assertEqual(GalvanizeTestQuestions.sample_sd(142, 250), 0.4964)
         self.assertEqual(GalvanizeTestQuestions.sd_of_sample_mean(142, 250), 0.0314)
         self.assertEqual(GalvanizeTestQuestions.confidence_interval(3486, 6014, .95), 0.073)

if __name__ == '__main__':
    unittest.main()
