
def verify_points(points, areas_array):

	points_x = points[0]
	points_y = points[1]
	
	for area in range(len(points_x)):
	
		if areas_array[area].is_in_area(points_x[area], points_y[area]):
			print("Digit ", area, "is correct. ")
		else:
			print("Digit ", area, "FUCK YOU.")
