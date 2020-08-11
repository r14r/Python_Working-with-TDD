def test_should_pass():
    pass

def test_should_raise_error():
    raise ValueError

def test_check_if_true_is_true():
    assert True == True

def inc(x):
    return x + 1


def test_check_if_inc_works():
    assert inc(3) == 5
