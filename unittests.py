import unittest
from helper import cutter, found_duplication, weight_input_calibrator, words_dict_gen
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

    def test_find(self) -> None:
        self.assertEqual(
            found_duplication({'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2, 'тебя люблю': 3, 'я тебя люблю': 3}},
                              {'max': 0},
                              ['я', 'тебя', 'люблю', 'я тебя', 'тебя люблю', 'я тебя люблю']), [('max', 12)])

        self.assertEqual(
            found_duplication({'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2, 'тебя люблю': 3, 'я тебя люблю': 3}},
                              {'max': 0},
                              ['я', 'не', 'люблю', 'я не', 'не люблю', 'я не люблю']), [('max', 3)])

        self.assertEqual(
            found_duplication({'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2, 'тебя люблю': 3, 'я тебя люблю': 3}},
                              {'max': 0},
                              ['2342324', '234234', '333', '2342324 234234', '234234 333', '2342324 234234 333']),
            [('max', 0)])

        self.assertEqual(
            found_duplication({'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2, 'тебя люблю': 3, 'я тебя люблю': 3}},
                              {'max': 0},
                              ['']), [('max', 0)])

    def test_reply(self) -> None:
        self.assertEqual(reply_output('я тебя люблю', {'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2,
                                                               'тебя люблю': 3, 'я тебя люблю': 3}}), ['max'])
        self.assertEqual(reply_output('', {'max': {}}), [])
        self.assertEqual(reply_output('', {'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2,
                                                   'тебя люблю': 3, 'я тебя люблю': 3}}), [])
        self.assertEqual(reply_output('ывппвыыва ываывавыоадл', {'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2,
                                                                         'тебя люблю': 3, 'я тебя люблю': 3}}), [])
        self.assertEqual(reply_output('2342324 234234 333', {'max': {'я': 1, 'тебя': 1, 'люблю': 2, 'я тебя': 2,
                                                                     'тебя люблю': 3, 'я тебя люблю': 3}}), [])

    def test_weight(self) -> None:
        self.assertEqual(weight_input_calibrator(['я', 'тебя', 'люблю']), {'я': 1, 'тебя': 1, 'люблю': 2})
        self.assertEqual(weight_input_calibrator(['ывппвыыва', 'ываывавыоадл']), {'ывппвыыва': 2, 'ываывавыоадл': 3})
        self.assertEqual(weight_input_calibrator(['2342324', '234234', '333']), {'2342324': 2, '234234': 2, '333': 1})
        self.assertEqual(weight_input_calibrator(['']), {})


    def test_dict_gen(self) -> None:
        self.assertEqual(words_dict_gen({'я': 1, 'не': 1, 'люблю': 2}, {'я': 1, 'тебя': 1, 'люблю': 2}),
                         {'я': 2, 'тебя': 1, 'люблю': 4, 'не': 1})
        self.assertEqual(words_dict_gen({}, {'я': 1, 'тебя': 1, 'люблю': 2}), {'я': 1, 'тебя': 1, 'люблю': 2})
        self.assertEqual(words_dict_gen({'ывппвыыва': 2, 'ываывавыоадл': 3}, {'я': 1, 'тебя': 1, 'люблю': 2}),
                         {'я': 1, 'тебя': 1, 'люблю': 2, 'ывппвыыва': 2, 'ываывавыоадл': 3})
        self.assertEqual(words_dict_gen({'2342324': 2, '234234': 2, '333': 1},  {'я': 1, 'тебя': 1, 'люблю': 2}),
                         {'я': 1, 'тебя': 1, 'люблю': 2, '2342324': 2, '234234': 2, '333': 1})


if __name__ == '__main__':
    unittest.main()
