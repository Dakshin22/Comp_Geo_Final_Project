public class Edge {
    public Point p0;
    public Point p1;
    public double value;

    Edge(Point _p0, Point _p1) {
        this.p0 = _p0;
        this.p1 = _p1;
        this.value = this.getXValue(this.getLowerPoint().y);
    }

    public Point getLowerPoint() {
        if (p0.y <= p1.y) {
            return p0;
        } else {
            return p1;
        }

    }

    public String toString() {
        String ret = "";
        ret = ret + "<" + this.p0.toString() + ", " + this.p1.toString() + ">";
        return ret;
    }

    public Point getUpperPoint() {
        if (p0.y > p1.y) {
            return p0;
        } else {
            return p1;
        }

    }

    public double getXValue(double yVal) {
        double slope = (this.p1.y - this.p0.y) / (this.p1.x - this.p0.x);
        return ((yVal - this.p1.y) / slope) + this.p1.x;
    }

}
