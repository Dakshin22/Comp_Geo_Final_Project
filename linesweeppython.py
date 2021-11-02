from sortedcontainers import sortedlist
from Point import Point
from Edge import Edge
from Event import Event
from heapq import *
# http://www.grantjenks.com/docs/sortedcontainers/
from sortedcontainers import *
from maxHeap import max_heap
from bintrees import *
#Qs how to randomize line segments
#horizontal lines
#How to implement line sweep status
def generateRandomSegments():
    edges = [
             Edge(Point(2,1), Point(1,4)),
             Edge(Point(3,3), Point(1,6)),
             Edge(Point(8,2), Point(4,6)),
             Edge(Point(5,3), Point(8,7)),
             Edge(Point(6,3), Point(9,6))
            ]

    return edges


def lineSweepIntersection(edges):
    eventQueue = getEvents(edges)
    heapify(eventQueue)
    currEvent = eventQueue[0]
    lineSweepStatus = SortedKeyList(key=lambda x: getXValue(x, currEvent.point.y))
    print(lineSweepStatus)
    i = 0
    while eventQueue:
        currEvent = heappop(eventQueue)
        yLevel = currEvent.point.y
        lineSweepStatus = SortedKeyList(lineSweepStatus, key=lambda x: getXValue(x, currEvent.point.y))
        if currEvent.category == 0:
            lineSweepStatus.add(currEvent.edge1)
        elif currEvent.category == 1:
            #print(currEvent.edge1 == Edge(Point(2,1), Point(1, 4)))
            lineSweepStatus.remove(currEvent.edge1)
        print(lineSweepStatus)
        i += 1

    
def getXValue(segment, yVal):
    slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x)
    return ((yVal - segment.p1.y )/ slope) + segment.p1.x

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
'''
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                pass
                #print(intersectionPoint)
'''

lineSweepIntersection(myEdges)