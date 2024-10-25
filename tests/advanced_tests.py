import unittest

from src.function import regex_has_a_special_prefix as checker

class Tests_advanced(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(checker("ab+", "a", 1)[0], ("YES"))
        self.assertEqual(checker("ab+", "b", 1)[0], ("YES"))
        self.assertEqual(checker("ab+c+", "a", 1)[0], ("YES"))
        self.assertEqual(checker("ab+c+", "b", 1)[0], ("YES"))
        self.assertEqual(checker("ab+c+", "c", 1)[0], ("YES"))

    def test_concatenation(self):
        self.assertEqual(checker("ab.", "a", 1)[0], ("YES"))
        self.assertEqual(checker("ab.", "b", 1)[0], ("NO"))
        self.assertEqual(checker("ab.c.", "c", 1)[0], ("NO"))

    def test_star(self):
        self.assertEqual(checker("ab+*", "a", 5)[0], ("YES"))
        self.assertEqual(checker("ab+*", "b", 5)[0], ("YES"))
        self.assertEqual(checker("ab.*", "a", 2)[0], ("NO"))
        self.assertEqual(checker("a**", "a", 10)[0], ("YES"))

    def test_regex_building(self):
        self.assertEqual(checker("ab+", "a", 1)[1], ("(a+b)"))
        self.assertEqual(checker("ab.", "a", 1)[1], ("ab"))
        self.assertEqual(checker("ab+*", "a", 1)[1], ("(a+b)*"))
        self.assertEqual(checker("ab+c.aba.*.bac.+.+*", "a", 1)[1], ("((a+b)c+a(ba)*(b+ac))*"))

    def test_combinations(self):
        self.assertEqual(checker("ab+c.aba.*.bac.+.+*", "a", 1)[0], ("YES"))
        self.assertEqual(checker("ab+c.aba.*.bac.+.+*", "a", 2)[0], ("YES"))
        self.assertEqual(checker("ab+c.aba.*.bac.+.+*", "a", 3)[0], ("NO"))
        self.assertEqual(checker("acb..bab.c.*.ab.ba.+.+*a.", "b", 2)[0], ("YES"))
        self.assertEqual(checker("acb..bab.c.*.ab.ba.+.+*a.", "b", 3)[0], ("NO"))
        self.assertEqual(checker("ab+cb+.*", "b", 5)[0], ("YES"))