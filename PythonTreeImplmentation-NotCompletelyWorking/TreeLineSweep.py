from Event import Event
from heapq import *
# http://www.grantjenks.com/docs/sortedcontainers/
# avl tree: https://github.com/Bibeknam/algorithmtutorprograms/blob/master/data-structures/avl-trees/avl_tree.py
from SortedListBasic import SortedListBasic
from AVLTree import Node, AVLTree

class TreeLineSweep:
    def __init__(self, edges):
        self.eventQueue = self.getEvents(edges)
        heapify(self.eventQueue)
        self.lineSweepStatus = AVLTree()
        self.intersections = set()

    def lineSweep(self):
        currEvent = self.eventQueue[0]
        currY = currEvent.point.y
        #print(lineSweepStatus)
        while self.eventQueue:
            currEvent = heappop(self.eventQueue)
            currY = currEvent.point.y
            #print(currEvent.category)
            if currEvent.category == 0:
                print("cat 0")
                print(self.lineSweepStatus.inorder_traverse())
                self.lineSweepStatus.insert(currEvent.edge1, currY)
                print(self.lineSweepStatus.inorder_traverse())
                predEdge = self.lineSweepStatus.predecessor(currEvent.edge1)
                sucEdge = self.lineSweepStatus.successor(currEvent.edge1)
                if predEdge:
                    #print(f"pred Edge {predEdge}")
                    intersection = predEdge.intersectionPoint(currEvent.edge1)
                    self.addIntersection(intersection, self.eventQueue,
                                    self.intersections, predEdge, currEvent.edge1)
                if sucEdge:
                    #print(f"suc Edge {sucEdge}")
                    intersection = sucEdge.intersectionPoint(currEvent.edge1)
                    self.addIntersection(intersection, self.eventQueue,
                                    self.intersections, currEvent.edge1, sucEdge)

            elif currEvent.category == 1:
                print("cat 1")
                predEdge = self.lineSweepStatus.predecessor(currEvent.edge1)
                sucEdge = self.lineSweepStatus.successor(currEvent.edge1)
                if predEdge and sucEdge:
                    intersection = predEdge.intersectionPoint(sucEdge)
                    self.addIntersection(intersection, self.eventQueue,
                                    self.intersections, predEdge, sucEdge)
                self.lineSweepStatus.delete(currEvent.edge1, currY)

            else:
                print("cat 2", currEvent.edge1, currEvent.edge2)
                #print("intersection event")
                self.lineSweepStatus.swapEdges(currEvent.edge1, currEvent.edge2, currY)
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

            #print(lineSweepStatus.toString(yVal=currY))
        return self.intersections
        #print(intersections)


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

