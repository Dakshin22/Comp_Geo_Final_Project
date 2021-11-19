from Edge import Edge

'''
Main data structure for line sweep status
Supports inserting, removing, finding successor and predecessor, and swapping two segments at a particular Y value
Maintains sorted data to store segments/edges
Linear time for most operations
'''
class SortedListBasic:
    def __init__(self):
        self.sortedList = []
    
    def __repr__(self):
        return str(self.sortedList)

    def toString(self, yVal):
        toPrint = self.sortedList[:]
        for i in range(len(self.sortedList)):
            toPrint[i] = (toPrint[i], getXValue(toPrint[i], yVal))
        return str(yVal) + str(toPrint)

    def add(self, value: Edge, yValue):
        idx = len(self.sortedList)
        self.sortedList.append(value)
        while idx > 0 and getXValue(self.sortedList[idx-1], yValue) > getXValue(self.sortedList[idx], yValue):
            self.swap(idx-1, idx)
            idx-=1

    def remove(self, value: Edge):
        self.sortedList.remove(value)

    def index(self, value: Edge):
        return self.sortedList.index(value)

    def predecessor(self, value: Edge):
        idx = self.index(value)
        if idx > 0:
            predIdx = idx - 1
            return self.sortedList[predIdx]
        else:
            return None
    
    def successor(self, value:Edge):
        idx = self.index(value)
        if idx < len(self.sortedList) - 1:
            sucIdx = idx + 1
            return self.sortedList[sucIdx]
        else:
            return None

    def swap(self, idx1, idx2):
        self.sortedList[idx2], self.sortedList[idx1] = self.sortedList[idx1], self.sortedList[idx2]

    def swapEdges(self, edge1, edge2, currY):
        if edge1 in self.sortedList:
            self.remove(edge1)
        if edge2 in self.sortedList:
            self.remove(edge2)
        if edge2 not in self.sortedList:
            self.add(edge2, currY + 0.01)
        if edge1 not in self.sortedList:
            self.add(edge1, currY + 0.01)

    def get(self, idx):
        return self.sortedList[idx]

def getXValue(segment, yVal):
    slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x)
    xVal =  ((yVal - segment.p1.y )/ slope) + segment.p1.x
    xVal = round(xVal, 2)
    return xVal