import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Edge> myEdgesList = new ArrayList<Edge>();
        Edge e1 = new Edge(new Point(2, 1), new Point(1, 4));
        Edge e2 = new Edge(new Point(8, 2), new Point(4, 6));
        Edge e3 = new Edge(new Point(6, 3), new Point(9, 6));
        Edge e4 = new Edge(new Point(5, 3), new Point(8, 7));
        Edge e5 = new Edge(new Point(3, 3), new Point(1, 6));
        myEdgesList.add(e1);
        myEdgesList.add(e2);
        myEdgesList.add(e3);
        myEdgesList.add(e4);
        myEdgesList.add(e5);

        LineSweep algo = new LineSweep(myEdgesList);
        long t1 = System.currentTimeMillis();
        algo.line_sweep();
        long t2 = System.currentTimeMillis(); 
        System.out.println(algo.intersections);
        System.out.println("runtime: " + (t2 - t1) + " ms");
    }

    
}
