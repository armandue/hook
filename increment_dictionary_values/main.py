import unittest
from unittest import TestCase


def increment_dictionary_values(d, i):
    new_d = d.copy()
    for k, v in new_d.items():
        new_d[k] = v + i
    return new_d


class TestIncrementDictionaryValues(TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


if __name__ == '__main__':
    unittest.main()
