class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __round__(self, ndigits):
        self.x = round(self.x, ndigits)
        self.y = round(self.y, ndigits)
    
    def __hash__(self):
        return hash((self.x, self.y))