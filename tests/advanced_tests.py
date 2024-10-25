import unittest

from src.function import regex_has_a_special_prefix as checker

class Tests_advanced(unittest.TestCase):

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
        self.assertEqual(checker("ab+1.1a.+1+*", "a", 10)[0], ("YES"))
        self.assertEqual(checker("ab+1.1a.+1+*", "b", 10)[0], ("YES"))