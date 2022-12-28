from chaosGame.point import Point
from random import uniform, randint

def generateRandomPoint(lowerBound: Point, upperBound: Point) -> Point:
		p: Point = Point(uniform(lowerBound.x, upperBound.x), uniform(lowerBound.y, upperBound.y))
		return p

def pointsToCoords(points: list) -> tuple:
	xCoords = []
	yCoords = []
	for point in points:
		xCoords.append(point.x)
		yCoords.append(point.y)
	return (xCoords, yCoords)
