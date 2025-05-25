#by default, every python file is like a pacakage which we can import.
# here, we're importing a function from another py file.

#1. import the function which we want to test in the test file which has to start with test_ or end with _test.py.
from base_file import a, b, add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers
 
print(a, b, add_two_numbers(a, b), subtract_two_numbers(a, b), multiply_two_numbers(a, b), divide_two_numbers(a, b))

# TESTING THE CODE

# pytest is a testing framework for python that allows us to write simple and scalable test cases.
# whatever file we want to test, has to start with test_ or end with _test.py.
# whatever we want to test, the function also has to start with test_.

#2. In this python file, we can write any function and speciy assert statements to check if the function is working as expected.

def test_a_functionality():
    assert add_two_numbers(2, 3) == 5 #assert is a function that checks if the condition is true or false
    #assert checks if LHS == RHS, do nothing if true, else raise an AssertionE  rror.

def test_b_functionality():
    assert subtract_two_numbers(5, 3) == 2