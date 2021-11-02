from sortedcontainers import sortedlist
from Point import Point
from Edge import Edge
from Event import Event
from heapq import *
# http://www.grantjenks.com/docs/sortedcontainers/
from sortedcontainers import *
from maxHeap import max_heap
from bintrees import *

def generateRandomSegments():
    edges = [Edge(Point(2,1), Point(1,4)),
             Edge(Point(3,3), Point(1,6)),
             Edge(Point(8,2), Point(4,6)),
             Edge(Point(5,3), Point(8,7)),
             Edge(Point(6,3), Point(9,6))
    ]

    return edges



def lineSweepIntersection(edges):
    eventQueue = getEvents(edges)
    lineSweepStatus = SortedList(edges, key=lambda x: x.p0.x)
    print(lineSweepStatus)
    heapify(eventQueue)
    print(eventQueue)

def getEvents(edges):
    # Event category 0 is bottom, 1 is top, 2 is intersection
    events = []
    for edge in edges:
        if edge.p0.y > edge.p1.y:
            events.append(Event(1, edge.p0, edge))
            events.append(Event(0, edge.p1, edge))
        else:
            events.append(Event(0, edge.p0, edge))
            events.append(Event(1, edge.p1, edge))

    return events

myEdges = generateRandomSegments()
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                print(intersectionPoint)

lineSweepIntersection(myEdges)