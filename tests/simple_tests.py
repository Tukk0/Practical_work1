import unittest

from src.function import regex_has_a_special_prefix as checker

class Tests_simple(unittest.TestCase):
    def test_one_letter(self):
        self.assertEqual(checker('a', 'a', 1)[0], ("YES"))
        self.assertEqual(checker('b', 'b', 1)[0], ("YES"))
        self.assertEqual(checker('c', 'c', 1)[0], ("YES"))
        self.assertEqual(checker('a*', 'a', 100)[0], ("YES"))
        self.assertEqual(checker('a*', 'b', 100)[0], ("NO"))

    def test_error(self):
        with self.assertRaises(ValueError):
            checker('a', 'd', 0)
        with self.assertRaises(ValueError):
            checker('a', '+', 1)
        with self.assertRaises(ValueError):
            checker('a', 'a', -1)
        with self.assertRaises(ValueError):
            checker('a', 'a', -12)
        with self.assertRaises(ValueError):
            checker('ab', 'a', 1)
        with self.assertRaises(ValueError):
            checker('a+', 'a', -1)
        with self.assertRaises(ValueError):
            checker('aa+a..', 'a', 1)
        with self.assertRaises(ValueError):
             checker('.', 'a', 1)
        with self.assertRaises(ValueError):
            checker("ab+a", 'a', 1)