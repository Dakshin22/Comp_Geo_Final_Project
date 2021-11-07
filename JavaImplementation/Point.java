

public class Point {
    public double x;
    public double y;

    Point(double _x, double _y)
    {
        this.x = _x;
        this.y = _y;
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
}