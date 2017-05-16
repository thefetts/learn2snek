import unittest
from code import fileio


class TestFileIO(unittest.TestCase):
    def test_itCanReadAFile(self):
        result = fileio.read_file('data.txt')
        self.assertEqual(result, ['Hi Jordan', 'This is a file', "Isn't it great?"])


if __name__ == '__main__':
    unittest.main()
