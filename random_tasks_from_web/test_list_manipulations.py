from list_manipulations import f_13, b

"""
def test_no_number_from_the_interval():
    pass


def test_one_number_from_the_interval():
    pass


def test_all_numbers_from_the_interval():
    pass


def test_interval_starts_and_ends_the_same_value():
    pass
"""

def test_interval_starts_from_bigger_number():
    res = f_13(b, 5, 0, 8)
    assert res == b

"""
def test_interval_with_floats():
    pass


def test_initial_list_with_floats():
    pass
"""


def test_empty_list():
    res = f_13([], 0, 5, 8)
    assert res == []


f_13(b, 0, 5, 8)
