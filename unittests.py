import unittest
from helper import cutter
class TestCutter(unittest.TestCase):
    # начинается с test_
    def test_cut(self):
        self.assertEqual(cutter('я тебя люблю'.split()), ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю', 'я тебя люблю'])
        self.assertEqual(cutter('I love you'.split()), ['I', 'love', 'you', 'I love', 'love you', 'I love you'])
        self.assertEqual(cutter(1234567890), [])

if __name__ == '__main__':
    unittest.main()