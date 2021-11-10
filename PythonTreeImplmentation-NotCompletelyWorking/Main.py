
from Edge import Edge
from Point import Point
import time
import random
from LineSweep import LineSweep


pointsSoFar = set()
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
    while len(randomEdges) < 5000:
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
    return randomEdges, bestCaseEdges, edges


def getRandomPoint(min_range_x, max_range_x, min_range_y, max_range_y):
    p = Point(random.uniform(min_range_x, max_range_x),
              random.uniform(min_range_y, max_range_y))
    while p in pointsSoFar:
        p = Point(random.uniform(min_range_x, max_range_x),
              random.uniform(min_range_y, max_range_y))
    pointsSoFar.add(p)
    round(p, 2)
    return p


myEdges, myBestEdges, simpleEdges = generateRandomSegments()
algo = LineSweep(myEdges)
start = time.time()
algo.lineSweep()
end = time.time()
print(f"runtime: {end - start}s")