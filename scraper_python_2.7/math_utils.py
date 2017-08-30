from utils import InputArgsException
import math

import numbers


def inLatLonHull(latLonHull, latLonPoint):
    return latLonPoint not in getLatLonHull(latLonHull + [latLonPoint])

def getLatLonHull(latLonPoints):
    res = []

    xyToLatLon = {}
    for entry in latLonPoints:
        xyToLatLon[getXY(entry, latLonPoints[0][0])] = entry

    xyRes = getConvexHull(xyToLatLon.keys())
    for xyPoint in xyRes:
        res.append(xyToLatLon[xyPoint])

    return res


def getConvexHull(points):
    invalidArgsExc = isValidArgsConvexHull(points)
    if (invalidArgsExc is not None):
        raise invalidArgsExc


    res = []

    leastXPoint = reduce(lambda x1, x2 : min(x1, x2), points)

    centerPoint = leastXPoint
    endPoint = (leastXPoint[0], leastXPoint[1] - .0000001)

    while (centerPoint not in res):
        res.append(centerPoint)

        stableVec = (endPoint[0] - centerPoint[0], endPoint[1] - centerPoint[1])
        leastCosOfVecs = 1
        newCenterPoint = None
        for point in points:
            if point == centerPoint or point == endPoint:
                continue
            else:
                iterVec = (point[0] - centerPoint[0], point[1] - centerPoint[1])
                curCosOfVecs = findCosOfVecs(stableVec, iterVec)

                if (curCosOfVecs == leastCosOfVecs):
                    raise InputArgsException("Collinear points in input array")
                elif (curCosOfVecs < leastCosOfVecs):
                    leastCosOfVecs = curCosOfVecs
                    newCenterPoint = point
        endPoint = centerPoint
        centerPoint = newCenterPoint

    return res

"""
def inHull(hull, point):
    return point not in getConvexHull(hull + [point])
"""

def findCosOfVecs(vec1, vec2):
    return ((vec1[0] * vec2[0] + vec1[1] * vec2[1])
            / (math.sqrt(vec1[0] ** 2 + vec1[1] ** 2) * math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)))




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

def getXYArr(coords, centerLat):
    res = []
    for point in coords:
        res.append(getXY(point, centerLat))
    return res
