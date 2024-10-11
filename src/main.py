from function import regex_is_correct
from function import regex_has_a_special_prefix as checker
checker("ab + c.aba. * .bac. + . + *", 'a', 2)
