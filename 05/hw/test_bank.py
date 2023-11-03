from bank import value

def test_bank_normal_cases():
    assert value("Hello") == 0
    assert value("Hello,") == 0
    assert value("Hi") == 20
    assert value("Hi!") == 20
    assert value("Guten Tag!") == 100
    assert value("hello") == 0
    assert value("hello,") == 0
    assert value("hi") == 20
    assert value("hi!") == 20
    

def test_bank_edge_cases():
    assert value(20) == 0
    assert value("!!!") == 0