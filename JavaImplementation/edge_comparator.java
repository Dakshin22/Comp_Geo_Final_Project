
import java.util.*;

/**
 * edge comparator for edges used in BST implementation
 * Has data member to change the current Y value.
 */
public class edge_comparator implements Comparator<Edge> {

    public double currY;

    edge_comparator() {
        this.currY = 0;
    }

    void setCurrY(double newY) {
        this.currY = newY;
    }

    @Override
    public int compare(Edge e_1, Edge e_2) {
        if (e_1.getXValue(currY) > e_2.getXValue(currY)) {
            return 1;
        }
        if (e_1.getXValue(currY) < e_2.getXValue(currY)) {
            return -1;
        }
        return 0;
    }
}
