import unittest

from code import interview


class TestInterview(unittest.TestCase):
    def test_interview_question(self):
        self.assertEqual(interview.question_1(), True)


if __name__ == '__main__':
    unittest.main()
