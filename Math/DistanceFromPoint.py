# Will calculate the distance from the root to a point
def DistanceFromRoot(PointX, PointY, PointZ):
	# Returns distance
	return (PointX**2 + PointY**2 + PointZ**2) ** 0.5

print(DistanceFromRoot(3.54, 3.54, 6))
