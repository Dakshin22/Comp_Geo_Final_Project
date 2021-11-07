from sortedcontainers import sortedlist
from Point import Point
from Edge import Edge
from Event import Event
from heapq import *
# http://www.grantjenks.com/docs/sortedcontainers/
# avl tree: https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/avl-trees/avl_tree.py
from SortedListBasic import SortedListBasic
import random
import time


def generateRandomSegments():
    edges = [
        Edge(Point(2, 1), Point(1, 4)),
        Edge(Point(3, 3), Point(1, 6)),
        Edge(Point(8, 2), Point(4, 6)),
        Edge(Point(5, 3), Point(8, 7)),
        Edge(Point(6, 3), Point(9, 6))
    ]

    edges2 = [
        Edge(Point(1.672, 0.141), Point(2.547, 3.187)),
        Edge(Point(4.499, 2.111), Point(2.082, 3.715)),
        Edge(Point(2.75, 3.94), Point(1.424, 2.449)),
        Edge(Point(2.203, 0.02), Point(4.132, 0.197)),
        Edge(Point(3.434, 4.911), Point(3.932, 1.038))
    ]
    randomEdges = []
    min_range = 0
    max_range = 1000
    while len(randomEdges) < 300:
        randomEdge = Edge(getRandomPoint(min_range, max_range, min_range,
                                               max_range), getRandomPoint(min_range, max_range, min_range,  max_range))
        if abs(randomEdge.p0.y - randomEdge.p1.y) > 5:
            randomEdges.append(randomEdge)
    #print(randomEdges)

    bestCaseEdges = []
    increment = 10
    i = 0
    while len(bestCaseEdges) < 500000:
        bestEdge = Edge(getRandomPoint(min_range, max_range, i, i + increment//2), getRandomPoint(
            min_range, max_range, i + increment//2 + 1, i + increment))

        bestCaseEdges.append(bestEdge)
        i+=increment
    return randomEdges, bestCaseEdges


def getRandomPoint(min_range_x, max_range_x, min_range_y, max_range_y):
    p = Point(random.uniform(min_range_x, max_range_x),
              random.uniform(min_range_y, max_range_y))
    round(p, 3)
    return p


def lineSweepIntersectionLinear(edges):
    #print(edges)
    eventQueue = getEvents(edges)
    heapify(eventQueue)
    currEvent = eventQueue[0]
    intersections = set()
    currY = currEvent.point.y
    lineSweepStatus = SortedListBasic()
    #print(lineSweepStatus)
    while eventQueue:
        currEvent = heappop(eventQueue)
        currY = currEvent.point.y
        #print(currEvent.category)
        if currEvent.category == 0:
            lineSweepStatus.add(currEvent.edge1, currY)
            predEdge = lineSweepStatus.predecessor(currEvent.edge1)
            sucEdge = lineSweepStatus.successor(currEvent.edge1)
            if predEdge:
                intersection = predEdge.intersectionPoint(currEvent.edge1)
                addIntersection(intersection, eventQueue,
                                intersections, predEdge, currEvent.edge1)
            if sucEdge:
                intersection = sucEdge.intersectionPoint(currEvent.edge1)
                addIntersection(intersection, eventQueue,
                                intersections, currEvent.edge1, sucEdge)

        elif currEvent.category == 1:
            predEdge = lineSweepStatus.predecessor(currEvent.edge1)
            sucEdge = lineSweepStatus.successor(currEvent.edge1)
            if predEdge and sucEdge:
                intersection = predEdge.intersectionPoint(sucEdge)
                addIntersection(intersection, eventQueue,
                                intersections, predEdge, sucEdge)
            lineSweepStatus.remove(currEvent.edge1)

        else:
            #print("intersection event")
            lineSweepStatus.swapEdges(currEvent.edge1, currEvent.edge2)
            predEdge = lineSweepStatus.predecessor(currEvent.edge2)
            if predEdge:
                intersection = predEdge.intersectionPoint(currEvent.edge2)
                addIntersection(intersection, eventQueue,
                                intersections, predEdge, currEvent.edge2)
            sucEdge = lineSweepStatus.successor(currEvent.edge1)
            if sucEdge:
                intersection = currEvent.edge1.intersectionPoint(sucEdge)
                addIntersection(intersection, eventQueue,
                                intersections, currEvent.edge1, sucEdge)

        #print(lineSweepStatus.toString(yVal=currY))
    return intersections
    #print(intersections)


def addIntersection(intersection, eventQueue, intersections, edge1, edge2):
    if intersection:
        if intersection not in intersections:
            intersections.add(intersection)
            heappush(eventQueue, Event(2, intersection, edge1, edge2))


def getXValue(segment, yVal):
    slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x)
    return ((yVal - segment.p1.y) / slope) + segment.p1.x


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


myEdges, myBestEdges = generateRandomSegments()
'''
intersections = set()
for e1 in myEdges:
    for e2 in myEdges:
        if e1 != e2:
            intersectionPoint = e1.intersectionPoint(e2)
            if intersectionPoint:
                intersections.add(intersectionPoint)
'''
#print(intersections)
start = time.time()
lineSweepIntersectionLinear(myEdges)
end = time.time()
print(f"runtime: {end - start}s")