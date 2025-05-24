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

    assert multiply_two_numbers(2, 3) == 6 #assert is a function that checks if the condition is true or false
    #assert checks if LHS == RHS, do nothing if true, else raise an AssertionE  rror.

def test_b_functionality():

    assert divide_two_numbers(6, 3) == 2 # is like a print statement that will print the message if the assertion fails.
    #assert add_two_numbers(2, 3) == 5
    #we can have multiple assert statements in a single function but typically we keep them separate for better readability. 

# #PS C:\Users\thosh\session_6_CI> pytest
# collected 4 items                                                                       
# notice, it has identified the test functions from different files as pytest identifies all the files which has test_ or _test in the name and finds out function which has test_ in the name.
# test_code.py ..                                                                   [ 50%]
# test_code_v2.py ..                                                                [100%] 

# ================================== 4 passed in 0.15s =================================== 

# def test_b_functionality():
#     assert divide_two_numbers(6, 3) == 1, "Division failed" # is like a print statement that will print the message if the assertion fails.
#  test_code_v2.py:24: AssertionError
# =============================== short test summary info ================================ 
# FAILED test_code_v2.py::test_b_functionality - AssertionError: Division failed
# ============================= 1 failed, 3 passed in 0.34s ==============================

# test_code.py ..                                                                
# test_code_v2.py .. these dots specify the number of functions and that our functions executed perefctly good.
# test_code.py .F, it will change to F if the test fails. (here, 2nd function of the test_code.py file failed)