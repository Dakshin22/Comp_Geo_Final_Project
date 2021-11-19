'''
Point class
* x and y track point coordinate values
* values are rounded to 2
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __round__(self, ndigits):
        self.x = round(self.x, ndigits)
        self.y = round(self.y, ndigits)
    
    def __hash__(self):
        return hash((self.x, self.y))