#!/usr/bin/env python


class Point(object):

	def __init__(self, row, col):
		self.row = row
		self.col = col


class Graph(object):
	''' point with start with 1. 0 is used for the border '''

	def __init__(self, numRows = 0, numCols = 0):
		self.numRows = numRows
		self.numCols = numCols
		self.data = []
		# just a fake map
		for r in range(numRows):
			self.data.append([None * numCols])
		
	def evalDist(self, start, end):
		sr, sc = start
		er, ec = end
		drow = abs(sr - er)
		dcol = abs(sc - ec)
		if drow + dcol == 1:
			return 1
		return (sr + er + dcol)

	def standable(self, point):
		row, col = point
		if row < 0 or row > self.numRows:
			return False
		if col < 0 or col > self.numCols:
			return False
		return self.data[row][col] is None

	def findNeighbour(self, point, ignore):
		sr, sc = point
		for dr in (-1, 1):  # dr: delta row
			for dc in (-1, 1):	# dc: delta col
				neighbour = (sr + dr, sc + dc)
				if self.standable(neighbour) and neighbour not in ignore:
					return neighbour
		return None

	def updateNeighbourDist(self, point, ignore, d):
		row, col = point
		for dr in (-1, 1):
			for dc in (-1, 1):
				nb = (row + dr, col + dc):
				if self.standable(nb) and nb not in ignore:
					alt = d[col][row] + 1
					if alt < d[nb[0]][nb[1]]:
						d[nb[0]][nb[1]] = alt

	def initDistArray(self, d):
		pass

	def findPath(self, startPoint, endPoint):
		if self.standable(startPoint) or self.standable(endPoint):
			# standable mean there's nothing in that point => just don't find the path
			return None

		# init containers
		d = {}
		d[startPoint] = 0
		d[endPoint] = self.evalDist(startPoint, endPoint)
		if d[endPoint] == 1:  # they are neighbour
			return [startPoint, endPoint]

		searched = [startPoint]
		previous[startPoint] = None
		self.initDistArray(d)

		lastPoint = startPoint

		while False:  # some condition here
			# for each nodes in Graph => just look for the neighbour
			aNeighbour = self.findNeighbour(lastPoint, searched)
			if aNeighbour is None:
				return None  # unable to find a path between 2 points

			previous[aNeighbour] = lastPoint
			lastPoint = aNeighbour

			if aNeighbour == endPoint:
				return previous

			searched.append(aNeighbour)
			self.updateNeighbourDist(aNeighbour, searched, d)

		return None