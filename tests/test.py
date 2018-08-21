"""
test module for hungarian.py
"""
import pytest
from hungarian import *

matrices = { 0: ([[62, 75, 80, 93, 95, 97],
                  [75, 80, 82, 85, 71, 97],
                  [80, 75, 81, 98, 90, 97],
                  [78, 82, 84, 80, 50, 98],
                  [90, 85, 85, 80, 85, 99],
                  [65, 75, 80, 75, 68, 96]],

                  543,

                  [(0, 4), (2, 3), (5, 5), (4, 0), (1, 1), (3, 2)]),

             1: ([[4, 2, 8],
                  [4, 3, 7],
                  [3, 1, 6]],

                  12,

                  [(0, 1), (1, 0), (2, 2)]),

             2: ([[62, 75, 80, 93, 0, 97],
                  [75, 0, 82, 85, 71, 97],
                  [80, 75, 81, 0, 90, 97],
                  [78, 82, 0, 80, 50, 98],
                  [0, 85, 85, 80, 85, 99],
                  [65, 75, 80, 75, 68, 0]],

                  523,

                  [(0, 3), (2, 4), (3, 0), (5, 2), (1, 5), (4, 1)]),
                  }


def test_hungarian_0():
    M = matrices[0]

    hungarian = Hungarian()
    hungarian.calculate(M[0], is_profit_matrix=True)

    assert M[1] == hungarian.get_total_potential()
    assert M[2] == hungarian.get_results()

def test_hungarian_1():
    M = matrices[1]

    hungarian = Hungarian()
    hungarian.calculate(M[0], is_profit_matrix=False)

    assert M[1] == hungarian.get_total_potential()
    assert M[2] == hungarian.get_results()

def test_hungarian_2():
    M = matrices[2]

    hungarian = Hungarian()
    hungarian.calculate(M[0], is_profit_matrix=True)

    assert M[1] == hungarian.get_total_potential()
    assert M[2] == hungarian.get_results()