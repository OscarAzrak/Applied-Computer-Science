import unittest
from checkfil8 import *

class TestAtom(unittest.TestCase):
    def test_endast_siffror(self):
        #Assume
        formel = "Aa"
        validator = Validator()

        #Action
        result = validator.atom_valid(formel)
        #Assert
        FormelError(result)

    def test_borjar_med_liten_bokstav(self):
        #Assume
        formel = "a12"
        validator = Validator()

        #Action
        result = validator.atom_valid(formel)
        #Assert
        FormelError(result)

    def test_borjar_inte_med_stor_bokstav(self):
        #Assume
        formel = "aa12"
        validator = Validator()

        #Action
        result = validator.atom_valid(formel)
        #Assert
        FormelError(result)

    def test_borjar_inte_med_stor_bokstav(self):
        #Assume
        formel = "aa12"
        validator = Validator()

        #Action
        result = validator.atom_valid(formel)
        #Assert
        FormelError(result)