import java.util.*;

/**
 * class for tree based linesweep algorithm Uses balanced BST (Red black tree)
 * for linesweep 
 * n = # segments, k = # intersections 
 * Worst Case: O((n + k) * log(n)) 
 * Best Case: O(n)
 */
public class OptimizedLineSweep {

    private TreeSet<Edge> lineSweepStatus;
    private edge_comparator cmp = new edge_comparator();
    private Queue<Event> eventQueue;
    public Set<Point> intersections;

    public OptimizedLineSweep(ArrayList<Edge> edges) {
        this.lineSweepStatus = new TreeSet<Edge>(cmp);
        this.eventQueue = new PriorityQueue<>(new event_comparator());
        ArrayList<Event> events = getEvents(edges);
        for (Event e : events) {
            eventQueue.add(e);
        }
        this.intersections = new HashSet<Point>();
    }

    public void line_sweep() {
        while (!eventQueue.isEmpty()) {
            Event currEvent = eventQueue.poll();
            cmp.currY = currEvent.point.y;
            if (currEvent.category == 0) {

                lineSweepStatus.add(currEvent.edge1);
                Edge predEdge = lineSweepStatus.lower(currEvent.edge1);
                Edge sucEdge = lineSweepStatus.higher(currEvent.edge1);
                if (predEdge != null) {
                    Point intersection = predEdge.intersectionPoint(currEvent.edge1);
                    this.addIntersection(intersection, predEdge, currEvent.edge1);
                }
                if (sucEdge != null) {
                    Point intersection = sucEdge.intersectionPoint(currEvent.edge1);
                    this.addIntersection(intersection, currEvent.edge1, sucEdge);
                }

            } else if (currEvent.category == 1) {
                Edge predEdge = lineSweepStatus.lower(currEvent.edge1);
                Edge sucEdge = lineSweepStatus.higher(currEvent.edge1);
                if (predEdge != null && sucEdge != null) {
                    Point intersection = predEdge.intersectionPoint(sucEdge);
                    this.addIntersection(intersection, predEdge, sucEdge);
                }
                lineSweepStatus.remove(currEvent.edge1);

            } else {

                swapEdges(currEvent.edge1, currEvent.edge2, cmp.currY);
                Edge predEdge = lineSweepStatus.lower(currEvent.edge2);
                if (predEdge != null) {
                    Point intersection = predEdge.intersectionPoint(currEvent.edge2);
                    addIntersection(intersection, predEdge, currEvent.edge2);
                }
                Edge sucEdge = lineSweepStatus.higher(currEvent.edge1);
                if (sucEdge != null) {
                    Point intersection = currEvent.edge1.intersectionPoint(sucEdge);
                    addIntersection(intersection, currEvent.edge1, sucEdge);
                }
            }
        }
    }

    /**
     * Swaps to edges in line sweep status by deleting both, then inserting them at
     * a slightly higher y value
     * O(log(n)) total
     * @param edge1
     * @param edge2
     * @param currY
     */
    public void swapEdges(Edge edge1, Edge edge2, double currY) {

        lineSweepStatus.remove(edge1);
        lineSweepStatus.remove(edge2);
        cmp.currY = currY + 0.1;
        lineSweepStatus.add(edge2);
        lineSweepStatus.add(edge1);

    }

    public void addIntersection(Point intersection, Edge edge1, Edge edge2) {
        if (intersection != null) {
            if (!intersections.contains(intersection)) {
                this.intersections.add(intersection);
                this.eventQueue.add(new Event(2, intersection, edge1, edge2));

            }
        }
    }

    public double getXValue(Edge segment, double yVal) {
        double slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x);
        return ((yVal - segment.p1.y) / slope) + segment.p1.x;
    }

    public ArrayList<Event> getEvents(ArrayList<Edge> edges) {
        // Event category 0 is bottom, 1 is top, 2 is intersection
        ArrayList<Event> events = new ArrayList<Event>();
        for (Edge edge : edges) {
            if (edge.p0.y > edge.p1.y) {
                events.add(new Event(1, edge.p0, edge, null));
                events.add(new Event(0, edge.p1, edge, null));
            } else {
                events.add(new Event(0, edge.p0, edge, null));
                events.add(new Event(1, edge.p1, edge, null));
            }
        }
        return events;
    }

    private class event_comparator implements Comparator<Event> {
        @Override
        public int compare(Event e_1, Event e_2) {
            if (e_1.value > e_2.value) {
                return 1;
            }
            if (e_1.value < e_2.value) {
                return -1;
            }
            return 0;
        }
    }

}
