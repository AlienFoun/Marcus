import unittest
from helper import cutter
from reply import reply_output


class TestCutter(unittest.TestCase):

    def test_cut(self) -> None:
        self.assertEqual(cutter(['я', 'тебя', 'люблю']),
                         ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю', 'я тебя люблю'])
        self.assertEqual(cutter(['I', 'love', 'you']),
                         ['I', 'love', 'you', 'I love', 'love you', 'I love you'])
        self.assertEqual(cutter(['Lorem', 'ipsum', 'dolor', 'sit', 'amet']),
                         ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'Lorem ipsum',
                          'ipsum dolor', 'dolor sit', 'sit amet', 'Lorem ipsum dolor',
                          'ipsum dolor sit', 'dolor sit amet', 'Lorem ipsum dolor sit',
                          'ipsum dolor sit amet', 'Lorem ipsum dolor sit amet'])
        self.assertEqual(cutter([]), [])


class TestReply(unittest.TestCase):

    def test_reply(self) -> None:
        self.assertEqual(reply_output('я тебя люблю', [['due', ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю',
                                                                'я тебя люблю']]]), ['due'])
        self.assertEqual(reply_output('', [['due', '']]), [])
        self.assertEqual(reply_output('', [['due', ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю',
                                                    'я тебя люблю']]]), [])


if __name__ == '__main__':
    unittest.main()
