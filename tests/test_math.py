import pytest

def test_addition():
    assert 1+1 ==2

def test_substraction():
    assert 1-1 == 0

#### if we want to run the same test procedure with multiple input combos?
####Sweet! Parameters are a great way to do data-driven testing.
@pytest.mark.parametrize(
    "a,b, expected",
    [(0,5,0),(1,5,5),(2,5,10),(3,5,15),(4,5,20)]
)

def test_multiplication(a,b, expected):
    assert a*b == expected

#pytest treats unhandled exceptions as test failures.
#def test_divide_byZero():
#    assert 1/0                  #test failed ZeroDivisionError: division by zero

#Use pytest.raises with the desired exception type
# to raise an exception correctly
def test_divide_byZero():
    with pytest.raises(ZeroDivisionError):
        1 / 0                                  #now the test passed
