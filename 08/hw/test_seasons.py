from seasons import f_minutes_to_words, f_vali_date
import pytest

def test_f_vali_date():
    assert f_vali_date("1989-05-29") == "1989-05-29"

    #assert f_vali_date("cat") == SystemExit
    #assert f_vali_date("2000-13-32") is ValueError
    #assert f_vali_date("!!!") is ValueError

def test():
    with pytest.raises(SystemExit) as sample:
        f_vali_date("cat")
    assert sample.type == SystemExit    
    


    
    