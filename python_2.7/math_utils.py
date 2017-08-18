from utils import InputArgsException
import math

import numbers

def getConvexHull(points):
    invalidArgsExc = isValidArgsConvexHull(points)
    if (invalidArgsExc is not None):
        raise invalidArgsExc

    xyToLatLon = {}

    for entry in points:
        xyToLatLon[getXY(entry)] = entry

    res = []

    leastX = reduce(lambda x1, x2 : min(x1, x2), map(lambda point: point[0], xyToLatLon.keys()))

    curPoint = leastX
    #line = getLine(firstpoint, slope=99999999)
    """
    while (firstpoint not in res and firstpoint != curPoint):
        res.append(curPoint)
        
        next = findNext(curPoint, line, points)
        
        curPoint = findNext[0]
        line = findNext[1]
    
    
    """




def isValidArgsConvexHull(points):
    if (isinstance(points, list)):
        if (len(points) < 3):
            return InputArgsException("There must be at least 3 points to create a convex hull.")
        for point in points:
            if (not isValidPoint(point)):
                return InputArgsException("Input to convex hull contains an "
                                            + "invalid point (2-tuple of real numbers): " + point)
        return None
    return InputArgsException("Input to convex hull must be a list of points (2-tuple of real numbers).")

def isValidPoint(point):
    if (isinstance(point, tuple)
            and len(point) is 2
            and isinstance(point[0], numbers.Real)
            and isinstance(point[1], numbers.Real)):
        return True
    else:
        return False

def getXY(coord, centerLat):
    # miles
    earthRad = 3958.8
    x = earthRad * coord[1] * math.cos(centerLat)
    y = earthRad * coord[0]

    return (x, y)


class Line():
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
        self.a = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        self.b = self.p1.y - (self.p1.x * self.a)

class Point():
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]