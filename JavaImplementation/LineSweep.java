import java.util.*;

public class LineSweep {
    private SortedList lineSweepStatus;
    private Queue<Event> eventQueue;
    public ArrayList<Point> intersections;

    public LineSweep(ArrayList<Edge> edges) {
        this.lineSweepStatus = new SortedList();
        this.eventQueue = new PriorityQueue<>(new event_comparator());
        ArrayList<Event> events = getEvents(edges);
        for (Event e : events) {
            eventQueue.add(e);
        }
        this.intersections = new ArrayList<Point>();
    }

    public void line_sweep()
    {
        while(!eventQueue.isEmpty())
        {
            Event currEvent = eventQueue.poll();
            double currY = currEvent.point.y;
            if (currEvent.category == 0)
            {}
            else if (currEvent.category == 1) {}
            else {}
        }
    }

    public void addIntersection(Point intersection, Edge edge1, Edge edge2)
    {
        if (Objects.isNull(intersection))
        {
            this.intersections.add(intersection);
            this.eventQueue.add(new Event(2, intersection, edge1, edge2));
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
