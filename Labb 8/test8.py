from linkedQFile import LinkedQ

class Validator:

    def atom_is_valid(self, atom):

        if atom.islower():
            return False

        if atom.isnumeric():
            return False

        return True



