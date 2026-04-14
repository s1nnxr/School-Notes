class Interval:
    empty = Interval()
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            self._a = None
            self._b = None
            return
        if a is None:
            raise ValueError("Minimal value (a) can not be None")
        b = b if b is not None else a
        if b < a:
            raise ValueError("Invalid interval where b < a")
        self._a = a
        self._b = b
        
    def is_empty(self):
        """
        vrací True, je-li prázdný
        """
        if self._a is not None:
            assert self._b is not None # testování invariantu
            return False
        return True
    
    @property
    def a(self):
        if self.is_empty():
            raise ValueError("Empty interval has not minimum")
        return self._a
    
    @property
    def b(self):
        if self.is_empty():
            raise ValueError("Empty interval has not minimum")
        return self._b
    
        
    def __bool__(self):
        return not self.is_empty()
        
    def length(self):
        """
        vrací délku intervalu (tj. b-a)
        """
        if self.is_empty():
            return 0
        return self._b - self._a
    
    def intersection(self, other:'Interval') -> 'Interval':
        """
        vrací průnik intervalů
        """
        if max(self._a, other._a) > min(self._b, other._b):
            return Interval()
        return Interval(max(self._a, other._a), min(self._b, other._b))
    
    def __repr__(self) -> str:
        if self:
            return f"({self._a}, {self._b})"
        else:
            return f"()"
        
    @staticmethod
    def get_empty():
        return Interval()
    
    
