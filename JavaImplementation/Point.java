
import java.util.*;
import java.math.*;

/**
 * Point class 
 * x and y track point coordinate values 
 * values are rounded to 2
 */
public class Point {
    public double x;
    public double y;

    Point(double _x, double _y) {
        this.x = round(_x, 2);
        this.y = round(_y, 2);
    }

    public String toString() {
        String ret = "";
        ret = ret + "(" + this.x + ", " + this.y + ")";
        return ret;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (other == null) {
            return false;
        }
        if (other instanceof Point) {
            Point test = (Point) other;
            if (this.x == test.x && this.y == test.y) {
                return true;
            }
        }
        return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    public static double round(double value, int places) {
        if (places < 0)
            throw new IllegalArgumentException();

        int next = (int) value;
        BigDecimal bd = new BigDecimal(next);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}