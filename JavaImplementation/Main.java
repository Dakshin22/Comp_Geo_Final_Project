import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Edge> myEdgesList = new ArrayList<Edge>();
        Edge e1 = new Edge(new Point(2, 1), new Point(3.21, 3.04));
        Edge e2 = new Edge(new Point(8, 2), new Point(4, 6));
        Edge e3 = new Edge(new Point(6, 3), new Point(6.5, 3.5));
        Edge e4 = new Edge(new Point(5, 3), new Point(8, 7));
        Edge e5 = new Edge(new Point(4, 2), new Point(1, 6));
        myEdgesList.add(e1);
        myEdgesList.add(e2);
        myEdgesList.add(e3);
        myEdgesList.add(e4);
        myEdgesList.add(e5);







        
        ArrayList<Edge> randomEdges = getRandomEdges(-10000, 10000, 7000);
        //System.out.println(randomEdges);
        OptimizedLineSweep algo = new OptimizedLineSweep(randomEdges);
        LineSweep normalAlgo = new LineSweep(randomEdges);
        long t1 = System.currentTimeMillis();
        algo.line_sweep();
        long t2 = System.currentTimeMillis();
        System.out.println("runtime: " + (t2 - t1) + " ms");
        //System.out.println(algo.intersections);
        t1 = System.currentTimeMillis();
        normalAlgo.line_sweep();
        t2 = System.currentTimeMillis();
        System.out.println("runtime2: " + (t2 - t1) + " ms");
        //System.out.println(normalAlgo.intersections);

        


    }



    public static ArrayList<Edge> getRandomEdges(double low, double high, int num) {
        ArrayList<Edge> randomEdges = new ArrayList<Edge>();
        while (randomEdges.size() < num) {
            Edge randomEdge = new Edge(getRandomPoint(low, high, low, high), getRandomPoint(low, high, low, high));
            if (Math.abs(randomEdge.p0.y - randomEdge.p1.y) > 1) {
                randomEdges.add(randomEdge);
            }
        }
        return randomEdges;
    }

    public static Point getRandomPoint(double min_range_x, double max_range_x, double min_range_y, double max_range_y) {

        Point p = new Point(getRandomValue(min_range_x, max_range_x), getRandomValue(min_range_y, max_range_y));
        return p;

    }

    public static double getRandomValue(double min_range, double max_range) {
        Random r = new Random();
        double randomValue = min_range + (max_range - min_range) * r.nextDouble();
        //System.out.println(randomValue);
        return randomValue;
    }

}
