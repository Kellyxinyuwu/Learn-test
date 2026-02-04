import pytest

@pytest.mark.regression
def test_regression():
    print("Test 1")

# deliberately let the task fail
@pytest.mark.xfail
def test_regression2():
    print("Test 1")
    assert 4==5

# run the regression test
# pytest -m regression 

# run the test that is not regression
# pytest -m "not regression"
# pytest -v -m "not regression", give a clear version which more info while running

# testcases/test_firstcode.py F.                                
# testcases/test_markersDemo.py x  
# failue and deliberately failure

@pytest.mark.sanity
def test_regression():
    print("Test 1")

# pytest -m "regression or sanity" -v