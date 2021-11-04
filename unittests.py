import unittest
from helper import cutter, found_duplication, weight_input_calibrator, words_dict_gen
from reply import reply_output


class Testing(unittest.TestCase):

    def test_cut(self) -> None:
        self.assertEqual(cutter(['I', 'love', 'you']),
                         ['love', 'you', 'I love', 'love you', 'I love you'])
        self.assertEqual(cutter(['Lorem', 'ipsum', 'dolor', 'sit', 'amet']),
                         ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'Lorem ipsum',
                          'ipsum dolor', 'dolor sit', 'sit amet', 'Lorem ipsum dolor',
                          'ipsum dolor sit', 'dolor sit amet', 'Lorem ipsum dolor sit',
                          'ipsum dolor sit amet', 'Lorem ipsum dolor sit amet'])
        self.assertEqual(cutter([]), [])

    def test_find(self) -> None:
        self.assertEqual(
            found_duplication({'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2, 'i love you': 3}},
                              {'max': 0},
                              ['love', 'you', 'i love', 'love you', 'i love you']), [('max', 9)])

        self.assertEqual(
            found_duplication({'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2, 'I love you': 3}},
                              {'max': 0},
                              ['dont', 'love', 'i dont', 'dont love', 'i dont love']), [('max', 1)])

        self.assertEqual(
            found_duplication({'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2, 'I love you': 3}},
                              {'max': 0},
                              ['2342324', '234234', '333', '2342324 234234', '234234 333', '2342324 234234 333']),
            [('max', 0)])

        self.assertEqual(
            found_duplication({'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2, 'I love you': 3}},
                              {'max': 0},
                              ['']), [('max', 0)])

    def test_reply(self) -> None:
        self.assertEqual(reply_output('i love you', {'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2,
                                                             'I love you': 3}}), ['max'])
        self.assertEqual(reply_output('', {'max': {}}), [])
        self.assertEqual(reply_output('', {'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2,
                                                   'I love you': 3}}), [])
        self.assertEqual(reply_output('fsjfjkffs fsfospfsfpsfkp', {'max': {'love': 1, 'you': 1, 'i love': 2,
                                                                           'love you': 2, 'I love you': 3}}), [])
        self.assertEqual(reply_output('2342324 234234 333', {'max': {'love': 1, 'you': 1, 'i love': 2, 'love you': 2,
                                                                     'I love you': 3}}), [])

    def test_weight(self) -> None:
        self.assertEqual(weight_input_calibrator(['love', 'you']), {'love': 1, 'you': 1})
        self.assertEqual(weight_input_calibrator(['fsjfjkffs', 'fsfospfsfpsfkp']), {'fsjfjkffs': 2, 'fsfospfsfpsfkp': 3})
        self.assertEqual(weight_input_calibrator(['2342324', '234234', '333']), {'2342324': 2, '234234': 2, '333': 1})
        self.assertEqual(weight_input_calibrator(['']), {})

    def test_dict_gen(self) -> None:
        self.assertEqual(words_dict_gen({'dont': 1, 'love': 1}, {'love': 1, 'you': 1}),
                         {'dont': 1, 'love': 2, 'you': 1})
        self.assertEqual(words_dict_gen({}, {'love': 1, 'you': 1}), {'love': 1, 'you': 1})
        self.assertEqual(words_dict_gen({'fsjfjkffs': 2, 'fsfospfsfpsfkp': 3}, {'love': 1, 'you': 1}),
                         {'love': 1, 'you': 1, 'fsjfjkffs': 2, 'fsfospfsfpsfkp': 3})
        self.assertEqual(words_dict_gen({'2342324': 2, '234234': 2, '333': 1}, {'love': 1, 'you': 1}),
                         {'love': 1, 'you': 1, '2342324': 2, '234234': 2, '333': 1})


if __name__ == '__main__':
    unittest.main()
