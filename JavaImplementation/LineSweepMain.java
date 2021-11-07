import java.util.ArrayList;

public class LineSweepMain {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        System.out.println("Here");

        long endTime = System.currentTimeMillis();

        System.out.println("That took " + (endTime - startTime) + " milliseconds");
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
