


intersections = set()
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                intersections.add(intersectionPoint)

