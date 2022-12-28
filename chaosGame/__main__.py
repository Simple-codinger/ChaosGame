from chaosGame.point import Point
from .helper import generateRandomPoint, pointsToCoords
from chaosGame.sierpinskiGenerator import SierpinskiGenerator
import argparse

XBOUND = 100
YBOUND = 100
SIZE = 20
N = 1000
OUTPUT = 'picture'

def generateTriangle(size: int) -> tuple:
	# generate initial Point
	a = generateRandomPoint(Point(0, 0), Point(XBOUND-size, YBOUND-size))
	b = Point(a.x + size, a.y)
	c = Point(a.x + ((b.x - a.x)/2), a.y + size)
	return (a, b, c);

def main():
	# argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--points', dest='amountPoints', type=int, help='amount of points to draw', default=N, required=False)
	parser.add_argument('-s', '--triangleSize', dest='triangleSize', type=int, help='size of the triangle', default=SIZE, required=False)
	parser.add_argument('-o', '--output', dest='outputType', type=str, help='type of output (possible values: picture, animation)', default=OUTPUT, required=False) 
	args = parser.parse_args()	
	
	amountPoints = args.amountPoints
	triangleSize = args.triangleSize
	outputType = args.outputType

	(a, b, c) = generateTriangle(triangleSize) 
	sg: SierpinskiGenerator = SierpinskiGenerator(a, b, c)
	sg.generateSierpinski(sg.startPoint, amountPoints)
	if outputType == 'picture':
		sg.draw()
	elif outputType == 'animation':
		sg.animate()

if __name__ == "__main__":
	main()
