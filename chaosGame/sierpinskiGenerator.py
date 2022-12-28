from chaosGame.point import Point
from chaosGame.helper import generateRandomPoint, pointsToCoords
from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SierpinskiGenerator():
	def __init__(self, a: Point, b: Point, c: Point)->None:
		self.a: Point = a
		self.b: Point = b
		self.c: Point = c
		self.startPoint: Point = self.generatePointInTriangle(a, b, c)
		self.points: list = []
	
	def generateSierpinski(self, startPoint: Point, n: int)->None:
		startPoint: Point = self.startPoint
		for i in range(n):
			corner: Point = (self.a, self.b, self.c)[randint(0, 2)]
			point: Point = Point((startPoint.x + corner.x)/2, (startPoint.y + corner.y)/2)
			self.points.append(point)
			startPoint = point

	def draw(self)->None:
		(tXCoords, tYCoords) = pointsToCoords([self.a, self.b, self.c])
		plt.plot(tXCoords, tYCoords, '.', color='red')
		(pXCoords, pYCoords) = pointsToCoords(self.points)
		plt.plot(pXCoords, pYCoords, '.', color='black')					
		plt.show()	

	def animate(self)->None:
		(tXCoords, tYCoords) = pointsToCoords([self.a, self.b, self.c])
		fig = plt.figure()
		graph, = plt.plot(tXCoords, tYCoords, '.', color='red')
		def animateCallback(i):
			(xCoord, yCoord) = pointsToCoords([self.points[i]])
			plt.plot([xCoord], [yCoord], '.', color='black')		
		ani = FuncAnimation(fig, animateCallback, frames=len(self.points), interval=5, repeat=False)
		plt.show()
	def generatePointInTriangle(self, a: Point, b: Point, c: Point) -> Point:
		# generatePoint
		point: Point = None 
		while True:
			point = generateRandomPoint(Point(a.x, a.y), Point(b.x, c.y))
			# check if point is in triangle
			det: float = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
			isInside: bool = \
			det * ((b.x - a.x) * (point.y - a.y) - (b.y - a.y) * (point.x - a.x)) >= 0 and \
			det * ((c.x - b.x) * (point.y - b.y) - (c.y - b.y) * (point.x - b.x)) >= 0 and \
			det * ((a.x - c.x) * (point.y - c.y) - (a.y - c.y) * (point.x - c.x)) >= 0 
			if isInside:
				break	
		return point


