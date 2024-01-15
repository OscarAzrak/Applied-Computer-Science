from lab8 import *
import unittest
"""
N
Au
H2
cr12
8
Cr0
Pb1
#
"""


def main():
    validator = Validator()

    formel = input().strip()
    while formel != "#":
        try:
            value = validator.atom_valid(formel)
            formel = input().strip()
        except SyntaxError:
            formel = input().strip()
            pass



if __name__ == "__main__":
    unittest.main()