import unittest

from syntax import *


class SyntaxTest(unittest.TestCase):

    def testSubjPred(self):
        """ Testar Subj och Pred """
        self.assertEqual(kollaGrammatiken("JAG VET"), "Följer syntaxen!")

    def testFelKonj(self):
        self.assertEqual(kollaGrammatiken("JAG VET MEN"), "Fel konjunktion: MEN före . ")

if __name__ == '__main__':
    unittest.main()

"""
Am243
Pu244
Cm247
Bk247
Cf251
Es252
Fm257
Md258
No259
Lr262
Rf265
Db268
Hs270
Sg271
Bh272
Mt276
Rg280
Ds281
Cn285
H
He
Li
Be
B
C
N
O
F
Ne
Na
Mg
Al
Si
P
S
Cl
K
Ar
Ca
Sc
Ti
V
Cr
Mn
Fe
Ni
Co
Cu
Zn
Ga
Ge
As
Se
Br
Kr
Rb
Sr
Y
Zr
Nb
Mo
Tc
Ru
Rh
Pd
Ag
Cd
In
Sn
Sb
I
Te
Xe
Cs
Ba
La
Ce
Pr
Nd
Pm
Sm
Eu
Gd
Tb
Dy
Ho
Er
Tm
Yb
Lu
Hf
Ta
W
Re
Os
Ir
Pt
Au
Hg
Tl
Pb
Bi
Po
At
Rn
Fr
Ra
Ac
Pa
Th
Np
U
Am
Pu
Cm
Bk
Cf
Es
Fm
Md
No
Lr
Rf
Db
Hs
Sg
Bh
Mt
Rg
Ds
Cn
#
"""