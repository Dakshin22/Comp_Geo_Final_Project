
import java.util.*;

public class SortedList {
    public ArrayList<Edge> sortedList;

    public SortedList()
    {
        this.sortedList = new ArrayList<Edge>();
    }

    public String toString(double yVal) {
        String ret = "[";
        for (Edge e : sortedList) {
            ret = ret + e.toString() + " " + e.getXValue(yVal) + ", ";

        }
        ret = ret + "]"+ yVal ;
        return ret;
    }

    public void add(Edge value, double yValue) {
        int idx = this.sortedList.size();
        this.sortedList.add(value);
        while (idx > 0
                && getXValue(this.sortedList.get(idx - 1), yValue) > getXValue(this.sortedList.get(idx), yValue)) {
            this.swap(idx - 1, idx);
            idx -= 1;
        }
    }

    public void swap(int idx1, int idx2) {

        Collections.swap(this.sortedList, idx1, idx2);
    }

    public void remove(Edge value) {
        this.sortedList.remove(value);
    }

    public int index(Edge value) {
        return this.sortedList.indexOf(value);
    }

    public void swapEdges2(Edge edge1, Edge edge2, double currY) {
        this.remove(edge1);
        this.remove(edge2);
        add(edge2, currY + 0.01);
        add(edge1, currY + 0.01);

    }

    public int swapEdges(Edge edge1, Edge edge2) {
        int edge1Idx = this.index(edge1);
        int edge2Idx = this.index(edge2);
        if(edge1Idx == -1 || edge2Idx == -1)
        {
            // System.out.println(edge1);
            // System.out.println(edge2);
            // if(edge1Idx == -1)
            // {
            //     System.out.println(edge1 + "is the problem");
            // }
            // else if(edge2Idx == -1)
            // {
            //     System.out.println(edge1 + "is the problem");
            // }
            return -1;
        }
        this.swap(edge1Idx, edge2Idx);
        return 1;
    }

    public Edge get(int idx) {
        return this.sortedList.get(idx);
    }

    public Edge predecessor(Edge value) {
        int idx = this.index(value);
        if (idx > 0) {
            int predIdx = idx - 1;
            return this.sortedList.get(predIdx);
        } else {
            return null;
        }
    }

    public Edge successor(Edge value) {
        int idx = this.index(value);
        if (idx < this.sortedList.size() - 1) {
            int sucIdx = idx + 1;
            return this.sortedList.get(sucIdx);
        } else {
            return null;
        }
    }

    public double getXValue(Edge segment, double yVal) {
        double slope = (segment.p1.y - segment.p0.y) / (segment.p1.x - segment.p0.x);
        return ((yVal - segment.p1.y) / slope) + segment.p1.x;
    }

}
