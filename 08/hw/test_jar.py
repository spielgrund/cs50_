from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12,0)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12
    with pytest.raises(ValueError, match="ValueError"):
        jar.deposit(1)
        #raise ValueError("ValueError")
    





def test_withdraw():
    jar = Jar(12,12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10)
    assert str(jar) == "🍪"
    
    with pytest.raises(ValueError):
        jar.withdraw(10)
        

