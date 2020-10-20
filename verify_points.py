import image_stat

def verify_points(points, password):

	points_x = points[0]
	points_y = points[1]
	
	for pass_digit in range(len(password)):
	
		if image_stat.areas_array[password[pass_digit]].is_in_area(points_x[pass_digit], points_y[pass_digit]):
			print("Digit ", pass_digit, "is correct. ")
		else:
			print("Digit ", pass_digit, "FUCK YOU.")
