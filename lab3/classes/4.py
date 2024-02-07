import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def dist(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(2, 5)
point2 = Point(4, 3)

point1.show()
point2.show()

distance_between_points = point1.dist(point2)
print("Distance between points:", distance_between_points)

point1.move(1, 1)
point1.show()
