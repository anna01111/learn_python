
class CombStr:
    def __init__(self, string):
        self.string = string

    def count_substrings(self, length):
        if length == 0:
            return 0

        substrings = []
        for i in range(len(self.string) - length + 1):
            substrings.append(self.string[i:i + length])

        substrings = set(substrings)

        return len(substrings)


s0 = CombStr('qqqqqqweqqq%')

print(s0.count_substrings(0))  # 0
print(s0.count_substrings(1))  # 4
print(s0.count_substrings(2))  # 5
print(s0.count_substrings(5))  # 7
print(s0.count_substrings(15))  # 0
