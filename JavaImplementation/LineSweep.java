import java.util.*;

public class LineSweep {
    private SortedList lineSweepStatus;
    private Queue<Event> eventQueue;
    public Set<Point> intersections;

    public LineSweep(ArrayList<Edge> edges) {
        this.lineSweepStatus = new SortedList();
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
            double currY = currEvent.point.y;
            if (currEvent.category == 0) {

                lineSweepStatus.add(currEvent.edge1, currY);
                Edge predEdge = lineSweepStatus.predecessor(currEvent.edge1);
                Edge sucEdge = lineSweepStatus.successor(currEvent.edge1);
                if (predEdge != null) {
                    Point intersection = predEdge.intersectionPoint(currEvent.edge1);
                    this.addIntersection(intersection, predEdge, currEvent.edge1);
                }
                if (sucEdge != null) {
                    Point intersection = sucEdge.intersectionPoint(currEvent.edge1);
                    this.addIntersection(intersection, currEvent.edge1, sucEdge);
                }

            } else if (currEvent.category == 1) {
                Edge predEdge = lineSweepStatus.predecessor(currEvent.edge1);
                Edge sucEdge = lineSweepStatus.successor(currEvent.edge1);
                if (predEdge != null && sucEdge != null) {
                    Point intersection = predEdge.intersectionPoint(sucEdge);
                    this.addIntersection(intersection, predEdge, sucEdge);
                }
                lineSweepStatus.remove(currEvent.edge1);

            } else {

                lineSweepStatus.swapEdges2(currEvent.edge1, currEvent.edge2, currY);

                    Edge predEdge = lineSweepStatus.predecessor(currEvent.edge2);
                    if (predEdge != null) {
                        Point intersection = predEdge.intersectionPoint(currEvent.edge2);
                        addIntersection(intersection, predEdge, currEvent.edge2);
                    }
                    Edge sucEdge = lineSweepStatus.successor(currEvent.edge1);
                    if (sucEdge != null) {
                        Point intersection = currEvent.edge1.intersectionPoint(sucEdge);
                        addIntersection(intersection, currEvent.edge1, sucEdge);
                    }

            }
        }
    }

    public void addIntersection(Point intersection, Edge edge1, Edge edge2) {
        if (intersection != null) {
            if (!intersections.contains(intersection)) {
                this.intersections.add(intersection);
                this.eventQueue.add(new Event(2, intersection, edge1, edge2));

            }
        }
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
