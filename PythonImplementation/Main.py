
from Edge import Edge
from Point import Point
import time
import random
from LineSweep import LineSweep


pointsSoFar = set()
def generateRandomSegments(case, numEdges):
    '''
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
    '''
    min_range = 0
    max_range = 1000
    edges = []
    if case == 2:

        while len(edges) < numEdges:
            randomEdge = Edge(getRandomPoint(min_range, max_range, min_range,
                                                max_range), getRandomPoint(min_range, max_range, min_range,  max_range))
            if abs(randomEdge.p0.y - randomEdge.p1.y) > 5:
                edges.append(randomEdge)
        #print(randomEdges)

    if case == 1:
        increment = 5
        i = 0
        while len(edges) < numEdges:
            bestEdge = Edge(getRandomPoint(min_range, max_range, i, i + increment//2), getRandomPoint(
                min_range, max_range, i + increment//2 + 1, i + increment))

            edges.append(bestEdge)
            i+=increment
    return edges


def getRandomPoint(min_range_x, max_range_x, min_range_y, max_range_y):
    p = Point(random.uniform(min_range_x, max_range_x),
              random.uniform(min_range_y, max_range_y))
    while p in pointsSoFar:
        p = Point(random.uniform(min_range_x, max_range_x),
              random.uniform(min_range_y, max_range_y))
    pointsSoFar.add(p)
    round(p, 2)
    return p

print("What type of line segments would you like to generate?\nEnter '1' - Best Case: Line Segments not intersecting, stacked on top of one another.\nEnter '2' - Average Case: Random segments with coordinates in the range (0, 0) to (1000, 1000)")
case = input()
while case != '1' and case != '2':
    print("Please select from the following. What type of line segments would you like to generate?\nEnter '1' - Best Case\nEnter '2' - Worst Case: ")
    case = input()
numEdges = 0
while numEdges <= 0:
    print("How many line segments would you like to generate for this test?\nEnter a positive integer: ")
    numEdges = int(input())
print("Generating segments and setting up linesweep...")
myEdges = generateRandomSegments(int(case), numEdges)

algo = LineSweep(myEdges)
print("running line sweep...")
start = time.time()
algo.lineSweep()
end = time.time()
print(f"runtime: {(end - start)*1000} ms")