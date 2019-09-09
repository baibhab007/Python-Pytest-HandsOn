####
Parametrized test function
Set up the environment. Use the command touch test_prog.py; pip3 install pytest.

Create a pytest program with a single parameterized test function named test_cube_it, which accepts a number and prints its cube.

Use an assert function to check if the calculated output matches the expected output.

The expected input-output pairs to be provided to the parameterized test function are:

(3, 27),
(4, 15),
(5, 125)
View the output by using python3 -m pytest -s test_prog.py.

The expected output is:

val^3: 27
val^3: 64
Fval^3: 125
=========== 1 failed, 2 passed ==========
####

import pytest

def cube_it(x):
    y = x*x*x
    return y

@pytest.mark.parametrize('x,y',
                        [
                            (3,27),
                            (4,15),
                            (5,125)
                        ]
                        )
def test_cube_it(x,y):
    print('val^3: ', cube_it(x))
    assert cube_it(x) == y
    
    

