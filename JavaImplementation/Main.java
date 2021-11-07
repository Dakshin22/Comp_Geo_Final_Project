import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Edge> myEdgesList = new ArrayList<Edge>();
        Edge e1 = new Edge(new Point(2, 1), new Point(1, 4));
        Edge e2 = new Edge(new Point(8, 2), new Point(4, 6));
        Edge e3 = new Edge(new Point(6, 3), new Point(9, 6));
        Edge e4 = new Edge(new Point(5, 3), new Point(8, 7));
        Edge e5 = new Edge(new Point(3, 3), new Point(1, 6));

        SortedList list = new SortedList();
        list.add(e1, e1.getLowerPoint().y);
        System.out.println(list.toString(e1.getLowerPoint().y));
        list.add(e2, e2.getLowerPoint().y);
        System.out.println(list.toString(e2.getLowerPoint().y));
        list.add(e3, e3.getLowerPoint().y);
        System.out.println(list.toString(e3.getLowerPoint().y));
        list.add(e4, e4.getLowerPoint().y);
        System.out.println(list.toString(e4.getLowerPoint().y));
        list.add(e5, e5.getLowerPoint().y);
        System.out.println(list.toString(e5.getLowerPoint().y));
        System.out.println(list.predecessor(e1));
        System.out.println(list.successor(e2));
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
}
