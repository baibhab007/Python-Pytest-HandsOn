####
Fixture: Instantiation order
Set up the environment.

Use the command touch test_prog.py; pip3 install pytest.

Create a pytest program with four different fixtures as per the following specifications:

fixture_sess: Session scope fixture
fixture_modl: Module scope fixture
fixture_clss : Class scope fixture
fixture_func: Function scope fixture
The fixture function should display the following during the tear-down phase:

fixture_sess - Session fixture complete
fixture_modl - Module fixture complete
fixture_clss - Class fixture complete
fixture_func - Function fixture complete
Create a test class TestClass with a single test function test_one() which uses all the fixtures.

Hint: Use the @pytest.mark.usefixture() decorator for this.

The test function should print "Inside test".

View the output by using python3 -m pytest -s test_prog.py
####

import pytest
@pytest.fixture(scope='session')
def fixture_sess():
  print('Session scope fixture')
def fixture_modl():
  print('Module scope fixture')
def fixture_clss():
  print('Çlass scope fixture')
def fixture_func():
  print('Function scope fixture')
  
def teardown_module(module):
    print('Session fixture complete')

class TestClass:
  @pytest.mark.usefixtures('fixture_sess', 'fixture_modl', 'fixture_clss', 'fixture_func')
  def test_one(self):
    print('Inside test')
