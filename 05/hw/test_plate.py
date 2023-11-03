from plate import is_valid

def test_plate_nrml_cases():
    assert is_valid("aa") is True
    assert is_valid("aaa") is True
    assert is_valid("aaaa") is True
    assert is_valid("aaaaa") is True
    assert is_valid("aaaaaa") is True
    assert is_valid("aa1") is True
    assert is_valid("aa11") is True
    assert is_valid("aa111") is True
    assert is_valid("aa1111") is True

def test_plate_false_cases():
    assert is_valid("1a") is False
    assert is_valid("11") is False
    assert is_valid("aa1a") is False
    assert is_valid("aaa1a") is False
    assert is_valid("aaaa1a") is False
    assert is_valid("aa0") is False
    assert is_valid("aa01") is False
    assert is_valid("aaaa01") is False
    assert is_valid("aaaaa0") is False

def test_edge_cases():
    assert is_valid("!!!") is False
    
    

