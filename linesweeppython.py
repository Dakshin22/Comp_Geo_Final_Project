from Point import Point
from Edge import Edge
def generateRandomSegments():
    edges = [Edge(Point(2,1), Point(1,4)),
             Edge(Point(3,3), Point(1,6)),
             Edge(Point(8,2), Point(4,6)),
             Edge(Point(5,3), Point(8,7)),
             Edge(Point(6,3), Point(9,6))
    ]

    return edges

myEdges = generateRandomSegments()
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                print(intersectionPoint)

