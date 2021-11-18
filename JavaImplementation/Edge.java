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

    public Point intersectionPoint(Edge other) {
        double Dx = p1.x - p0.x;
        double Dy = p1.y - p0.y;
        double Rx = other.p1.x - other.p0.x;
        double Ry = other.p1.y - other.p0.y;
        // solve for s and t
        double Q0x = other.p0.x;
        double Q0y = other.p0.y;
        double P0x = p0.x;
        double P0y = p0.y;
        double s = (Dy * (Q0x - P0x) - Dx * (Q0y - P0y)) / ((Dx * Ry) - (Dy * Rx));
        if (s < 0 || s > 1) {

            return null;
        }
        double t = (Q0x - P0x + (Rx * s)) / Dx;
        if (t < 0 || t > 1) {

            return null;
        }
        // plug in t value to find intersection point using P = P0 + Dt
        double intersectionX = P0x + (t * Dx);
        double intersectionY = P0y + (t * Dy);

        Point intersection = new Point(intersectionX, intersectionY);
        return intersection;
    }

    public double getXValue(double yVal) {
        double slope = (this.p1.y - this.p0.y) / (this.p1.x - this.p0.x);
        return ((yVal - this.p1.y) / slope) + this.p1.x;
    }

}
