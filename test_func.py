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

@pytest.mark.skip(reason="no run")
def test_add_string1():
    assert func.add('Bye','World') == 'HelloWorld'

@pytest.mark.skipif(sys.version_info > (3, 3),reason="do not run")
def test_add_string2():
    assert func.add('Bye','World') == 'ByeWorld'
