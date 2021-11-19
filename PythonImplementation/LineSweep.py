from Event import Event
from heapq import *

from SortedListBasic import SortedListBasic

'''
class for linesweep algorithm
* Uses Sorted List
* Worst Case: O((n + k) * n)
* Best Case: O(n)
'''
class LineSweep:
    def __init__(self, edges):
        self.eventQueue = self.getEvents(edges)
        heapify(self.eventQueue)
        self.lineSweepStatus = SortedListBasic()
        self.intersections = set()

    def lineSweep(self):
        currEvent = self.eventQueue[0]
        currY = currEvent.point.y
        while self.eventQueue:
            currEvent = heappop(self.eventQueue)
            currY = currEvent.point.y
            if currEvent.category == 0:
                self.lineSweepStatus.add(currEvent.edge1, currY)
                predEdge = self.lineSweepStatus.predecessor(currEvent.edge1)
                sucEdge = self.lineSweepStatus.successor(currEvent.edge1)
                if predEdge:
                    intersection = predEdge.intersectionPoint(currEvent.edge1)
                    self.addIntersection(intersection, self.eventQueue,
                                         self.intersections, predEdge, currEvent.edge1)
                if sucEdge:
                    intersection = sucEdge.intersectionPoint(currEvent.edge1)
                    self.addIntersection(intersection, self.eventQueue,
                                         self.intersections, currEvent.edge1, sucEdge)

            elif currEvent.category == 1:
                predEdge = self.lineSweepStatus.predecessor(currEvent.edge1)
                sucEdge = self.lineSweepStatus.successor(currEvent.edge1)
                if predEdge and sucEdge:
                    intersection = predEdge.intersectionPoint(sucEdge)
                    self.addIntersection(intersection, self.eventQueue,
                                         self.intersections, predEdge, sucEdge)
                self.lineSweepStatus.remove(currEvent.edge1)

            else:
                self.lineSweepStatus.swapEdges(
                    currEvent.edge1, currEvent.edge2, currY)
                predEdge = self.lineSweepStatus.predecessor(currEvent.edge2)
                if predEdge:
                    intersection = predEdge.intersectionPoint(currEvent.edge2)
                    self.addIntersection(intersection, self.eventQueue,
                                         self.intersections, predEdge, currEvent.edge2)
                sucEdge = self.lineSweepStatus.successor(currEvent.edge1)
                if sucEdge:
                    intersection = currEvent.edge1.intersectionPoint(sucEdge)
                    self.addIntersection(intersection, self.eventQueue,
                                         self.intersections, currEvent.edge1, sucEdge)

        return self.intersections

    def addIntersection(self, intersection, eventQueue, intersections, edge1, edge2):
        if intersection:
            if intersection not in intersections:
                intersections.add(intersection)
                heappush(eventQueue, Event(2, intersection, edge1, edge2))

    def getXValue(self, segment, yVal):
        slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x)
        return ((yVal - segment.p1.y) / slope) + segment.p1.x

    def getEvents(self, edges):
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
