class P2:
    def __init__(self,x):
        self.x = x
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if (x < 0):
            self._x = 0
        elif (x > 1000):
            self._x = 1000
        else:
            self._x = x
            
p2 = P2(1001)
print(p2.x)

p2.x = -12
print(p2.x)
