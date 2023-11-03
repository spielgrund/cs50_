class Jar:
    def __init__(self, capacity=12, size=0):
        if 0 < capacity:
            self._capacity = capacity
            self._size = size
        else:
            raise ValueError("Capacity needs > 0")
        

    def __str__(self):
        return "🍪"*self._size
        #return f"{self._size}/{self._}"
        

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("ValueError")
        else:
            self._size += n
        

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("ValueError")
        else:
            self._size -= n
        

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter    # the property decorates with `.setter` now
    def capacity(self, value):   # name, e.g. "attribute", is the same
        self._capacity = value   # the "value" name isn't special


    @property
    def size(self):
        return self._size
    
    @size.setter    # the property decorates with `.setter` now
    def size(self, value):   # name, e.g. "attribute", is the same
        self._size = value   # the "value" name isn't special



