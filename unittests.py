import unittest
from helper import cutter
class TestCutter(unittest.TestCase):
    # начинается с test_
    def test_cut(self):
        self.assertEqual(cutter(['я', 'тебя', 'люблю']), ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю', 'я тебя люблю'])
        self.assertEqual(cutter(['I', 'love', 'you']), ['I', 'love', 'you', 'I love', 'love you', 'I love you'])
        self.assertEqual(cutter(['Lorem', 'ipsum', 'dolor', 'sit', 'amet']), ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'Lorem ipsum',
                                                                              'ipsum dolor', 'dolor sit', 'sit amet', 'Lorem ipsum dolor',
                                                                              'ipsum dolor sit', 'dolor sit amet', 'Lorem ipsum dolor sit',
                                                                              'ipsum dolor sit amet', 'Lorem ipsum dolor sit amet'])
        self.assertEqual(cutter(1234567890), [])
        self.assertEqual(cutter([]),[])

if __name__ == '__main__':
    unittest.main()