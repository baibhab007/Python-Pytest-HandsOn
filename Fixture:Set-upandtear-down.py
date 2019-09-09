####
Set up the environment. Use the command touch test_prog.py; pip3 install pytest.

Create a pytest program with a single fixture named fixture_example and a test function test_one().

The fixture function should print "Setup phase" in the setup phase, and "Teardown phase" in the teardown phase.

The test function should print "Inside test".

View the output by using python3 -m pytest -s test_prog.py.

The expected output is:

Setup phase
Inside test
Teardown phase
####

import pytest
@pytest.fixture
def fixture_example():
    print("Setup phase")
    yield fixture_example
    print("Teardown phase")
    
def test_one(fixture_example):
    print("Inside test")
