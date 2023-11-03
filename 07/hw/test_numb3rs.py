from numb3rs import validate

def test_validate_nrml():
    assert validate("192.168.1.1") is True
    assert validate("127.0.0.1") is True
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False
    assert validate("cat") is False

def test_validate_edgecases():
    assert validate("127...") is False
    assert validate("!!!") is False