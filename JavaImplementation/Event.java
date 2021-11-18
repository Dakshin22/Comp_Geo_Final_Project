public class Event {
    int category;
    Point point;
    Edge edge1;
    Edge edge2;
    double value;

    Event(int _category, Point _point, Edge _edge1, Edge _edge2) {
        this.category = _category;
        this.point = _point;
        this.edge1 = _edge1;
        this.edge2 = _edge2;
        this.value = this.point.y;

    }

    public String toString() {
        String ret = "";
        if (this.category == 0) {
            ret = ret + "<bottom, Point: " + this.point + " Edge 1: " + this.edge1 + ", Edge 2: " + this.edge2 + ">";

        } else if (this.category == 1) {
            ret = ret + "<top, Point: " + this.point + " Edge 1: " + this.edge1 + ", Edge 2: " + this.edge2 + ">";

        }
        return ret;

    }

}
