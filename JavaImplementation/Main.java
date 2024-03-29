import java.util.*;

public class Main {
    
    /*
    Main runner code to run linesweep algorithm according to user choices
    */
    public static void main(String[] args) {


        Scanner scanner = new Scanner(System.in);
        System.out.println(
                "What type of line segments would you like to generate?\nEnter 1 - Best Case: Line Segments not intersecting, stacked on top of one another.\nEnter 2 - Average Case: Random segments");
        int choice = scanner.nextInt();
        while (choice != 1 && choice != 2) {
            System.out.println(
                    "Please select from the following. What type of line segments would you like to generate?\nEnter 1 - Best Case\nEnter 2 - Worst Case: ");
            choice = scanner.nextInt();
        }
        int numEdges = 0;
        while (numEdges <= 0) {
            System.out.println(
                    "How many line segments would you like to generate for this test?\nEnter a positive integer: ");
            numEdges = scanner.nextInt();
        }
        int algorithm;
        System.out.println("Run tree based or array based algorithm?\nEnter 1 - Tree Based\nEnter 2 - Array Based");
        algorithm = scanner.nextInt();
        while (algorithm != 1 && algorithm != 2) {
            System.out.println(
                    "Please select from the following. Run tree based or array based algorithm?\nEnter 1 - Tree Based\nEnter 2 - Array Based");
            algorithm = scanner.nextInt();
        }
        scanner.close();
        if (choice == 1)
            System.out.println("Generating segments for best case...");
        else
            System.out.println("Generating segments for average case...");

        ArrayList<Edge> randomEdges = getRandomEdges(0, 1000, numEdges, choice);


        if (algorithm == 1) {
            System.out.println("Setting up Tree Based line sweep...");
            OptimizedLineSweep algo = new OptimizedLineSweep(randomEdges);
            System.out.println("Running Line sweep. Please wait for algorithm to finish...");
            long t1 = System.currentTimeMillis();
            algo.line_sweep();
            long t2 = System.currentTimeMillis();
            System.out.println("Algorithm done! Here is your runtime...");
            System.out.println("runtime: " + (t2 - t1) + " ms");
        }

        else {
            System.out.println("Setting up Array Based line sweep...");
            LineSweep normalAlgo = new LineSweep(randomEdges);
            System.out.println("Running Line sweep. Please wait for algorithm to finish...");
            long t11 = System.currentTimeMillis();
            normalAlgo.line_sweep();
            long t22 = System.currentTimeMillis();
            System.out.println("Algorithm done! Here is your runtime...");
            System.out.println("runtime: " + (t22 - t11) + " ms");
        }
    }

    /**
     * Generates random segments for best case and average case segments
     * @param low - minimum value for points
     * @param high - maximum value for points
     * @param num - number of points
     * @param choice - best or worst case? 1 - best, 2 - worst
     * @return randomEdges
     */
    public static ArrayList<Edge> getRandomEdges(double low, double high, int num, int choice) {

        ArrayList<Edge> randomEdges = new ArrayList<Edge>();
        if (choice == 2)

        {
            while (randomEdges.size() < num) {
                Edge randomEdge = new Edge(getRandomPoint(low, high, low, high), getRandomPoint(low, high, low, high));
                if (Math.abs(randomEdge.p0.y - randomEdge.p1.y) > 1) {
                    randomEdges.add(randomEdge);
                }
            }
        }

        else if (choice == 1) {
            double increment = 2;
            int i = 0;
            while (randomEdges.size() < num) {
                Edge bestEdge = new Edge(getRandomPoint(low, high, i, i + increment / 2),
                        getRandomPoint(low, high, i + increment / 2 + 1, i + increment));

                randomEdges.add(bestEdge);
                i += increment;
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
        return randomValue;
    }

}
