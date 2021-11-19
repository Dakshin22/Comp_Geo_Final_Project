
'''
This is the code for the brute force algorithm. It is not used in main.py, and was not used in experimentation
'''
intersections = set()
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                intersections.add(intersectionPoint)

