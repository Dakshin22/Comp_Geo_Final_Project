from Point import Point
from Edge import Edge

class Event:
    def __init__(self, category, point: Point, edge1: Edge, edge2=None):
        self.category = category
        self.point = point
        self.edge1 = edge1
        self.edge2 = edge2

    def __lt__(self, other):
        return self.point.y < other.point.y

    def __repr__(self):
        ret = ''
        if self.category == 0:
            ret+=f"<bottom, Point: {self.point}, Edge 1: {self.edge1}, Edge2: {self.edge2}>"
        elif self.category == 1:
            ret+=f"<top, Point: {self.point}, Edge 1: {self.edge1}, Edge2: {self.edge2}>"
        else:
            ret+=f"<intersection, Point: {self.point}, Edge 1: {self.edge1}, Edge2: {self.edge2}>"
        return ret
        
    