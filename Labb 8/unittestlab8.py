import unittest
from lab8ny1 import *


class TestAtom(unittest.TestCase):

    def test_it_will_reject_if_first_symbol_is_number(self):
        formel = "1"
        q = skapaQ(formel)
        result = checkAtom(q, formel)
        self.assertEqual(result, "Saknad stor bokstav vid radslutet " + formel)

    def test_it_will_reject_if_first_letter_is_small(self):
        formel = "oa"
        q = skapaQ(formel)
        result = checkAtom(q, formel)

        self.assertEqual(result, "Saknad stor bokstav vid radslutet " + formel)

    def test_it_will_reject_if_first_number_is_one_or_smaller(self):
        formel = "Cr0"
        q = skapaQ(formel)
        result = checkAtom(q, formel)

        self.assertEqual(result, "För litet tal vid radslutet ")

    def test_it_will_reject_if_first_number_is_one_but_there_are_no_numbers_after_that(self):
        formel = "Cr1"
        q = skapaQ(formel)
        result = checkAtom(q, formel)

        self.assertEqual(result, "För litet tal vid radslutet ")

    def test_it_will_accept_a_valid_formel(self):
        formel = "Cr12"
        q = skapaQ(formel)
        result = checkAtom(q, formel)
        self.assertEqual(result, "Formeln är syntaktiskt korrekt")


