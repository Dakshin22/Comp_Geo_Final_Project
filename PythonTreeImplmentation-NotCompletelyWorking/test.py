from AVLTree import AVLTree
from Edge import Edge
from Point import Point

tree = AVLTree()
tree.insert(Edge(Point(2, 1), Point(1, 4)), currY = 3.2)
tree.insert(Edge(Point(3, 3), Point(1, 6)),currY = 3.2)
tree.insert(Edge(Point(8, 2), Point(4, 6)),currY = 3.2)
tree.insert(Edge(Point(5, 3), Point(8, 7)),currY = 3.2)
tree.insert(Edge(Point(6, 3), Point(9, 6)),currY = 3.2)
tree.remove(Edge(Point(6, 3), Point(9, 6)),currY = 3.2)
node1 = tree.find(Edge(Point(8, 2), Point(4, 6)),currY = 3.2)
node2 = tree.find(Edge(Point(5, 3), Point(8, 7)),currY = 3.2)
if node1 and node2:
        tree.swap_nodes(node1, node2)
print(tree.preorder(tree.rootNode))