import unittest
from lab8ny1 import *


class TestAtom(unittest.TestCase):

    def test_it_ge_fel_om_forsta_symbol_ar_siffra(self):
        formel = "1"
        q = skapaQ(formel)
        result = checkAtom(q)
        self.assertEqual(result, "Saknad stor bokstav vid radslutet " + formel)
        
    def test_ge_fel_om_forsta_symbol_ar_liten_bokstav(self):
        formel = "oa"
        q = skapaQ(formel)
        result = checkAtom(q)
        self.assertEqual(result, "Saknad stor bokstav vid radslutet " + formel)
        
    def test_ge_fel_om_forsta_siffra_ar_1_eller_mindre(self):
        formel0 = "Cr0"
        q0 = skapaQ(formel0)
        result0 = checkAtom(q0)
        self.assertEqual(result0, "För litet tal vid radslutet ")

        formel1 = "Cr1"
        q1 = skapaQ(formel1)
        result1 = checkAtom(q1)
        self.assertEqual(result1, "För litet tal vid radslutet ")

    def test_ger_fel_om_forsta_siffra_ar_noll_men_det_finns_flera_siffror_efter(self):
        formel1 = "Cr01"
        q = skapaQ(formel1)
        result = checkAtom(q)
        self.assertEqual(result, "För litet tal vid radslutet 1")

        formel2 = "Cr02"
        q2 = skapaQ(formel2)
        result2 = checkAtom(q2)
        self.assertEqual(result2, "För litet tal vid radslutet 2")

        formel3 = "Cr03"
        q3 = skapaQ(formel3)
        result3 = checkAtom(q3)
        self.assertEqual(result3, "För litet tal vid radslutet 3")
        
    def test_acceptera_gilltig_atom(self):
        formellista = ["N","Au","H2","P21","Ag3","Fe12","Xx5"]
        for formel in formellista:
            q = skapaQ(formel)
            result = checkAtom(q)
            self.assertEqual(result, "Formeln är syntaktiskt korrekt")


if __name__ == '__main__':
    unittest.main()
