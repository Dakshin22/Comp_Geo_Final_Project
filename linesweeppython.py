from sortedcontainers import sortedlist
from Point import Point
from Edge import Edge
from Event import Event
from heapq import *
# http://www.grantjenks.com/docs/sortedcontainers/
#avl tree: https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/avl-trees/avl_tree.py
from sortedcontainers import *
from maxHeap import max_heap
from bintrees import *
from SortedListBasic import SortedListBasic
#Qs how to randomize line segments
#horizontal lines
#How to implement line sweep status
currY = 0

def generateRandomSegments():
    edges = [
             Edge(Point(2,1), Point(1,4)),
             Edge(Point(3,3), Point(1,6)),
             Edge(Point(8,2), Point(4,6)),
             Edge(Point(5,3), Point(8,7)),
             Edge(Point(6,3), Point(9,6))
            ]

    edges2 = [
             Edge(Point(2,1), Point(5,6)),
             Edge(Point(10,2), Point(1,6)),
             Edge(Point(8,2), Point(4,6)),
             Edge(Point(50,3), Point(8,7)),
             Edge(Point(6,3), Point(9,6))
            ]

    return edges

def lineSweepIntersectionLinear(edges):
    print(edges)
    eventQueue = getEvents(edges)
    heapify(eventQueue)
    currEvent = eventQueue[0]
    intersections = set()
    currY = currEvent.point.y
    lineSweepStatus = SortedListBasic()
    print(lineSweepStatus)
    i = 0
    while eventQueue:
        currEvent = heappop(eventQueue)
        currY = currEvent.point.y
        print(currEvent.category)
        if currEvent.category == 0:
            lineSweepStatus.add(currEvent.edge1, currY)
            idx = lineSweepStatus.index(currEvent.edge1)
            predIdx = lineSweepStatus.predecessor(currEvent.edge1)
            sucIdx = lineSweepStatus.successor(currEvent.edge1)
            if predIdx:
                predEdge = lineSweepStatus.get(predIdx)
                intersection = predEdge.intersectionPoint(currEvent.edge1)
                #print(intersection, lineSweepStatus.get(predIdx), lineSweepStatus.get(idx))
                addIntersection(intersection, eventQueue, intersections, predEdge, currEvent.edge1)

            if sucIdx:
                
                sucEdge = lineSweepStatus.get(sucIdx)
                intersection = sucEdge.intersectionPoint(currEvent.edge1)
                #print(intersection, lineSweepStatus.get(predIdx), lineSweepStatus.get(idx))
                addIntersection(intersection, eventQueue, intersections, currEvent.edge1, sucEdge)

                    
        elif currEvent.category == 1:
            #print(currEvent.edge1 == Edge(Point(2,1), Point(1, 4)))
            #lineSweepStatus = SortedKeyList(lineSweepStatus, key=lambda x: getXValue(x, currEvent.point.y))
            idx = lineSweepStatus.index(currEvent.edge1)
            predIdx = lineSweepStatus.predecessor(currEvent.edge1)
            sucIdx = lineSweepStatus.successor(currEvent.edge1)
            if predIdx and sucIdx:
                predEdge = lineSweepStatus.get(predIdx)
                sucEdge = lineSweepStatus.get(sucIdx)
                intersection = predEdge.intersectionPoint(sucEdge)
                #print(intersection, lineSweepStatus.get(predIdx), lineSweepStatus.get(sucIdx))
                addIntersection(intersection, eventQueue, intersections, predEdge, currEvent.edge1)

            lineSweepStatus.remove(currEvent.edge1)
        
        else:
            print("intersection event")
            idx1 = lineSweepStatus.index(currEvent.edge1)
            idx2 = lineSweepStatus.index(currEvent.edge2)
            print(idx1, idx2)
            lineSweepStatus.swap(idx1, idx2)
            predIdx = lineSweepStatus.predecessor(currEvent.edge2)
            if predIdx:
                predEdge = lineSweepStatus.get(predIdx)
                intersection = predEdge.intersectionPoint(currEvent.edge2)
                #print(intersection, predEdge, currEvent.edge2)
                addIntersection(intersection, eventQueue, intersections, predEdge, currEvent.edge2)

            sucIdx = lineSweepStatus.successor(currEvent.edge1)
            if sucIdx:
                sucEdge = lineSweepStatus.get(sucIdx)
                intersection = currEvent.edge1.intersectionPoint(sucEdge)
                #print(intersection, currEvent.edge2,  sucEdge)
                addIntersection(intersection, eventQueue, intersections, currEvent.edge1, sucEdge)

        print(lineSweepStatus.toString(yVal=currY))
    print(intersections)

def addIntersection(intersection, eventQueue, intersections, edge1, edge2):
    if intersection:
        if intersection not in intersections:
            intersections.add(intersection)
            heappush(eventQueue, Event(2, intersection, edge1, edge2))


def lineSweepIntersectionWithTree(edges):
    eventQueue = getEvents(edges)
    heapify(eventQueue)
    currEvent = eventQueue[0]
    intersections = set()
    currY = currEvent.point.y
    lineSweepStatus = SortedKeyList(key=lambda x: getXValue(x, currY))
    print(lineSweepStatus)
    i = 0
    while eventQueue:
        currEvent = heappop(eventQueue)
        currY = currEvent.point.y
        
        if currEvent.category == 0:
            #lineSweepStatus = SortedKeyList(lineSweepStatus, key=lambda x: getXValue(x, currEvent.point.y))
            lineSweepStatus.add(currEvent.edge1)
            idx = lineSweepStatus.index(currEvent.edge1)
            predIdx, sucIdx = idx - 1, idx + 1
            if 0 <= predIdx < len(lineSweepStatus):
                intersections.add(lineSweepStatus[predIdx].intersectionPoint(lineSweepStatus[idx]))
            if 0 <= sucIdx < len(lineSweepStatus):
                intersections.add(lineSweepStatus[sucIdx].intersectionPoint(lineSweepStatus[idx]))
        elif currEvent.category == 1:
            #print(currEvent.edge1 == Edge(Point(2,1), Point(1, 4)))
            #lineSweepStatus = SortedKeyList(lineSweepStatus, key=lambda x: getXValue(x, currEvent.point.y))
            idx = lineSweepStatus.index(currEvent.edge1)
            predIdx, sucIdx = idx - 1, idx + 1
            if 0 <= predIdx < len(lineSweepStatus) and 0 <= sucIdx < len(lineSweepStatus):
                intersections.add(lineSweepStatus[predIdx].intersectionPoint(lineSweepStatus[sucIdx]))
            lineSweepStatus.remove(currEvent.edge1)
        else:
            #lineSweepStatus = SortedKeyList(lineSweepStatus, key=lambda x: getXValue(x, currEvent.point.y+.01))
            print("intersection event")
            idx1 = lineSweepStatus.index(currEvent.edge1)
            idx2 = lineSweepStatus.index(currEvent.edge2)
            predIdx1, sucIdx1 = idx1 - 1, idx1 + 1
            if 0 <= predIdx1 < len(lineSweepStatus) and 0 <= sucIdx1 < len(lineSweepStatus):
                intersections.add(lineSweepStatus[predIdx1].intersectionPoint(lineSweepStatus[sucIdx1]))
            predIdx2, sucIdx2 = idx2 - 1, idx2 + 1
            if 0 <= predIdx2 < len(lineSweepStatus) and 0 <= sucIdx2 < len(lineSweepStatus):
                intersections.add(lineSweepStatus[predIdx2].intersectionPoint(lineSweepStatus[sucIdx2]))

        print(lineSweepStatus)

    intersections.remove(None)
    print(intersections)

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

lineSweepIntersectionLinear(myEdges)