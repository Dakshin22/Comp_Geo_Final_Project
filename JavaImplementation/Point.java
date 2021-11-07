
import java.util.*;
import java.math.*;

public class Point {
    public double x;
    public double y;

    Point(double _x, double _y)
    {
        this.x = round(_x, 2);    
        this.y = round(_y, 2);
    }

    public String toString()
    {
        String ret = "";
        ret = ret + "(" + this.x + ", " + this.y + ")";
        return ret;
    }

    public boolean equals(Point other) {
        return this.x == other.x && this.y == other.y;
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();
    
        BigDecimal bd = BigDecimal.valueOf(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}