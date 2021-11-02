from Point import Point

class Edge:
    def __init__(self, p0: Point, p1: Point):
        self.p0 = p0
        self.p1 = p1
    
    def __repr__(self):
        return f'<{self.p0}, {self.p1}>'

    def __eq__(self, other):
        return self.p0 == other.p0 and self.p1 == other.p1

    # Should return the intersection point or null, if no intersection exists.
    def intersectionPoint(self, other):
        # Should return the intersection point or null, if no intersection exists.
        Dx = self.p1.x - self.p0.x
        Dy = self.p1.y - self.p0.y
        Rx = other.p1.x - other.p0.x
        Ry = other.p1.y - other.p0.y
        #solve for s and t
        Q0x = other.p0.x
        Q0y = other.p0.y
        P0x = self.p0.x
        P0y = self.p0.y
        s = (Dy * (Q0x - P0x) - Dx*(Q0y - P0y))/((Dx * Ry) - (Dy * Rx))

        if(s < 0 or s > 1):
            return None

        t = (Q0x - P0x + (Rx * s))/Dx

        if(t < 0 or t > 1):
            return None
        
        # plug in t value to find intersection point using P = P0 + Dt
        intersectionX = P0x + (t * Dx)
        intersectionY = P0y + (t * Dy)

        intersection = Point(intersectionX, intersectionY)
        return intersection

