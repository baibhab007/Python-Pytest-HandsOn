# Python-Pytest-HandsOn

Pytest

Pytest Fixtures
There will be times when we need to do things before and after a test like setting up and releasing of resources.

Fixtures can be used to achieve these tasks and allow the tester to focus on the real test instead of setting up the environment.

A fixture represents a state of the program.

pip install pytest

Example:
1st file(func.py) :
def mult(x,y=4):
    return x*y

def add(x,y=4):
    return x+y

2nd file(test_func.py) :
import func
import pytest
import sys
@pytest.mark.number
def test_add():
    assert func.add(5,6) == 11
    assert func.add(9) == 13

@pytest.mark.number
def test_mult():
    assert func.mult(3,4) == 12
    assert func.mult(6) == 24

@pytest.mark.string
def test_add_string():
    assert func.add('Hello','World') == 'HelloWorld'
	print('--------------------')
	
@pytest.mark.skip(reason="do not run")
def test_add_string1():
    assert func.add('Bye','World') == 'ByeWorld'
	
@pytest.mark.skipif(sys.version_info > (3, 3),reason="do not run")
def test_add_string2():
    assert func.add('Bye','World') == 'ByeWorld'

Execute : pytest test_func.py -v / pytest test_func.py -v :: test_add / pytest -v -k "add" / pytest -v -k "add or string" / pytest -v -m number / pytest -v -x /
		  pytest -v -x --tb=no / 	pytest -v --maxfail=2 / pytest -v -s / pytest -v --capture=no / pytest -v -q
		  

		  
Instead of writing separate test functions, we could also write a single function with parametrize marker
---------------------------------------------------------------------------------------------------------
1st file(func.py) :
def add(x,y):
    return x+y
	
2nd file(test_func.py) :
import func
import pytest
@pytest.mark.parametrize('num1,num2,result',
						 [
							(7,3,10),
							('Hello', ' World', 'Hello World'),
							(10.5,25.5,36)
						 ]
						 )
def test_add(num1, num2, result):
	assert func.add(num1, num2) == result

	
When setting a db connection using setup and teardown methods
-------------------------------------------------------------
1st file(func.py) :
import json
class studentDB:
    def __init__(self):
        self.__data=None

    def connect(self,data_file):
        with open(data_file) as json_file:
            self.__data=json.load(json_file)

    def get_data(self,name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student

    def close(self):
        pass
		
2nd file(data.json) :
{
  "students": [
    {
      "id": 1,
      "name": "Scott",
      "result": "pass"
    },
    {
      "id": 2,
      "name": "Mark",
      "result": "fail"
    }
  ]
}

3rd file(test_func.py) :
from func import studentDB
import pytest

db=None
def setup_module(module):
    print('setup')
    global db
    db = studentDB()
    db.connect('data.json')

def teardown_module(module):
    print('teardown')
    db.close()

def test_scott_data():
    scott_data=db.get_data('Scott')
    assert scott_data['id']==1
    assert scott_data['name']=='Scott'
    assert scott_data['result']=='pass'

def test_mark_data():
    mark_data=db.get_data('Mark')
    assert mark_data['id']==2
    assert mark_data['name']=='Mark'
    assert mark_data['result']=='fail'
	

When setting up db connection using fixtures
--------------------------------------------
1st file(func.py) :
import json
class studentDB:
    def __init__(self):
        self.__data=None

    def connect(self,data_file):
        with open(data_file) as json_file:
            self.__data=json.load(json_file)

    def get_data(self,name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student

    def close(self):
        pass
		
2nd file(data.json) :
{
  "students": [
    {
      "id": 1,
      "name": "Scott",
      "result": "pass"
    },
    {
      "id": 2,
      "name": "Mark",
      "result": "fail"
    }
  ]
}

3rd file(test_func.py) :
from func import studentDB
import pytest
@pytest.fixture(scope='module')
def db():
    print('setup')
    db = studentDB()
    db.connect('data.json')
    yield db
    print('teardown')
    db.close()

def test_scott_data(db):
    scott_data=db.get_data('Scott')
    assert scott_data['id']==1
    assert scott_data['name']=='Scott'
    assert scott_data['result']=='pass'

def test_mark_data(db):
    mark_data=db.get_data('Mark')
    assert mark_data['id']==2
    assert mark_data['name']=='Mark'
    assert mark_data['result']=='fail'
	
