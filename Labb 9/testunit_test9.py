import unittest
from lab9 import *


class TestAtom(unittest.TestCase):

    def test_ge_fel_om_forsta_symbol_ar_siffra(self):
        formel = "2"
        q = skapaQ(formel)
        result = checkMol(q)
        self.assertEqual(result, "Felaktig gruppstart vid radslutet 2")
        
    def test_ge_fel_om_forsta_symbol_ar_liten_bokstav(self):
        formel1 = "oa"
        q1 = skapaQ(formel1)
        result1 = checkMol(q1)
        self.assertEqual(result1, "Saknad stor bokstav vid radslutet " + formel1)

        formel2 = "Nacl"
        q2 = skapaQ(formel2)
        result2 = checkMol(q2)
        self.assertEqual(result2, "Saknad stor bokstav vid radslutet cl")

    def test_ge_fel_om_forsta_siffra_ar_1_eller_mindre(self):
        formel0 = "Lv0"
        q0 = skapaQ(formel0)
        result0 = checkMol(q0)
        self.assertEqual(result0, "För litet tal vid radslutet ")

        formel1 = "Lv1"
        q1 = skapaQ(formel1)
        result1 = checkMol(q1)
        self.assertEqual(result1, "För litet tal vid radslutet ")

    def test_ger_fel_om_forsta_siffra_ar_noll_men_det_finns_flera_siffror_efter(self):
        formel1 = "Lv01"
        q = skapaQ(formel1)
        result = checkMol(q)
        self.assertEqual(result, "För litet tal vid radslutet 1")

        formel2 = "Lv02"
        q2 = skapaQ(formel2)
        result2 = checkMol(q2)
        self.assertEqual(result2, "För litet tal vid radslutet 2")

        formel3 = "Lv03"
        q3 = skapaQ(formel3)
        result3 = checkMol(q3)
        self.assertEqual(result3, "För litet tal vid radslutet 3")

    def test_ge_fel_om_atom_ej_finns_i_lista(self):
        formel = "C(Xx4)5"
        q = skapaQ(formel)
        result = checkMol(q)
        self.assertEqual(result, "Okänd atom vid radslutet 4)5")

    def test_ge_fel_om_molekyls_slutparentes_ej_har_siffra(self):
        formel = "C(OH4)C"
        q = skapaQ(formel)
        result = checkMol(q)
        self.assertEqual(result, "Saknad siffra vid radslutet C")

    def test_ge_fel_om_molekyls_ej_har_slutparentes(self):
        formel = "C(OH4C"
        q = skapaQ(formel)
        result = checkMol(q)
        self.assertEqual(result, "Saknad högerparentes vid radslutet ")

    def test_ge_fel_om_finns_slutparentes_men_ej_startparantes(self):
        formel1 = "H2O)Fe"
        q1 = skapaQ(formel1)
        result1 = checkMol(q1)
        self.assertEqual(result1, "Felaktig gruppstart vid radslutet )Fe")

        formel2 = ")"
        q2 = skapaQ(formel2)
        result2 = checkMol(q2)
        self.assertEqual(result2, "Felaktig gruppstart vid radslutet )")

        formel3 = "(Cl)2)3"
        q3 = skapaQ(formel3)
        result3 = checkMol(q3)
        self.assertEqual(result3, "Felaktig gruppstart vid radslutet )3")


        
    def test_acceptera_gilltig_atom(self):
        formellista = ["Na","H2O","Si(C3(COOH)2)4(H2O)7","Na332"]
        for formel in formellista:
            q = skapaQ(formel)
            result = checkMol(q)
            self.assertEqual(result, "Formeln är syntaktiskt korrekt")


if __name__ == '__main__':
    unittest.main()
