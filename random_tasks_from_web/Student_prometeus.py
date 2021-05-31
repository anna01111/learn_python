conf = {
    'exam_max': 30,
    'lab_max': 7,
    'lab_num': 10,
    'k': 0.61,
    }


class Student:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.lab_mark = [0 for item in range(10)]
        self.exam_mark = 0

    def make_lab(self, m, n=-1):
        if n == -1:
            n = self.lab_mark.index(0)

        if m < 0:
            return self
        if n < 0 or n > (self.config['lab_num'] - 1):
            return self
        if m > self.config['lab_max']:
            m = self.config['lab_max']

        self.lab_mark[n] = m

        return self

    def make_exam(self, m):

        if m > self.config['exam_max']:
            m = self.config['exam_max']

        self.exam_mark = m

        return self

    def is_certified(self):

        max_mark = self.config['lab_max'] * self.config['lab_num'] + self.config['exam_max']
        sum_mark = sum(self.lab_mark) + self.exam_mark

        prohidnii_bal = max_mark * self.config['k']

        result = sum_mark >= prohidnii_bal

        return sum_mark, result


oleg = Student('Oleg', conf)
print(oleg.lab_mark)
oleg.make_lab(7)
oleg.make_lab(8, 0)
oleg.make_lab(7)
oleg.make_lab(10, 7)
oleg.make_lab(7, 1)
oleg.make_lab(5)
oleg.make_lab(6.5)

oleg.make_exam(30)

print(oleg.is_certified())

