import unittest
from lab8 import *
from linkedQFile import LinkedQ
q = LinkedQ()

formel = "Cr01"
for elem in formel:
    q.enqueue(elem)

validator = Validator()

try:
    value = validator.atom_valid(formel)
except FormelError:
    pass



""""
class testAtom(unittest.TestCase):
    def test_om_inget_stort_bokstav_i_borjan(self):
        #Assume
        formel = "a"
        
        #Action

        #Assert

"""


