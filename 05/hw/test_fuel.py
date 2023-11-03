from fuel import convert, gauge
 

def test_fuel_nrml_cases():
    assert convert("1/4") == 25
    assert convert("0/5") == 0
    assert convert("1/1") == 100

def test_fuel_exept_cases():
    assert convert(1/4) == TypeError
    assert convert("cat") == ValueError
    assert convert("4/0") == ZeroDivisionError

def test_edge_cases():
    assert convert("!!!!")
