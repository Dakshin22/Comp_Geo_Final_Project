
import java.util.*;
import java.math.*;

public class TreeSetTest {
    public TreeSet<Edge> edgeTree;
    private edge_comparator cmp = new edge_comparator();

    TreeSetTest(ArrayList<Edge> edges)
    {
        
        this.edgeTree = new TreeSet<Edge>(cmp);
        cmp.currY = 3.7;
        System.out.println(cmp.currY);
        for(Edge e: edges)
            {
                edgeTree.add(e);
            }
    }

    public void print()
    {
       Iterator<Edge> it = edgeTree.iterator();
       while(it.hasNext())
        {
            Edge currEdge = it.next();
            System.out.println(currEdge.value);
            System.out.print(currEdge);
        }
        
    }


}
