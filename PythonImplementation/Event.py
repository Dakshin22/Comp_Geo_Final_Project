from Point import Point
from Edge import Edge
'''
Event class
* Keeps track of event values, point represents the point that event represents.
* Event category 0 is bottom, 1 is top, 2 is intersection
* edge2 is only non-null for intersection
'''
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
        
    