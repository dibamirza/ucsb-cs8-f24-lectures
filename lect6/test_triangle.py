# test_triangle.py
# test all the functiosn in triangle.py
from triangle import *

# unit test is_valid_triangle function
def test_is_valid_triangle_0():
    actual = is_valid_triangle(1, 2, 3)
    expected = False
    if actual == expected:
        print("PASSED: is_valid_triangle(1, 2, 3)")
    else:
        print(f"FAILED: is_valid_triangle(1, 2, 3): {actual=} {expected=}")


def test_is_valid_triangle_1():
    actual = is_valid_triangle(2, 2, 3)
    expected = True
    if actual == expected:
        print("PASSED: is_valid_triangle(2, 2, 3)")
    else:
        print(f"FAILED: is_valid_triangle(2, 2, 3): {actual=} {expected=}")


def test_is_valid_triangle_2():
    actual = is_valid_triangle(3, 1, 2)
    expected = False
    if actual == expected:
        print("PASSED: is_valid_triangle(3, 1, 2)")
    else:
        print(f"FAILED: is_valid_triangle(3, 1, 2): {actual=} {expected=}")

def test_is_valid_triangle_3():
    actual = is_valid_triangle(1, 4, 2)
    expected = False
    if actual == expected:
        print("PASSED: is_valid_triangle(1, 4, 2)")
    else:
        print(f"FAILED: is_valid_triangle(1, 4, 2): {actual=} {expected=}")

def test_get_triangle_type_0():
    actual = get_triangle_type(1, 1, 1)
    expected = "Equilateral"
    if actual == expected:
        print("PASSED: get_triangle_type(1, 1, 1)")
    else:
        print(f"FAILED: get_triangle_type(1, 1, 1): {actual=} {expected=}")


def test_get_triangle_type_1():
    actual = get_triangle_type(5, 2, 2)
    expected = "Isosceles"
    if actual == expected:
        print("PASSED: get_triangle_type(5, 2, 2)")
    else:
        print(f"FAILED: get_triangle_type(5, 2, 2): {actual=} {expected=}")

  

    
test_is_valid_triangle_0()
test_is_valid_triangle_1()
test_is_valid_triangle_2()
test_is_valid_triangle_3()
test_get_triangle_type_0()
test_get_triangle_type_1()
