
class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False

        if len(self) % len(s) == 0:
            n = int(len(self) / len(s))
            extended_s = s * n
            if self == extended_s:
                return True
        return False

    def is_palindrom(self):
        x = self.lower()

        y = [letter for letter in x if letter != ' ']

        if y[::-1] == y:
            return True
        else:
            return False


p = SuperStr('123_321')

print(p.is_palindrom())


