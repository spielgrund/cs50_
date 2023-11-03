from twttr import shorten

def test_square_alpha():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""

def test_square_num():
    assert shorten(20) == 20 

    