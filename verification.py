import image_stat
import preproc
import map_to_img
import find_fixations
import verify_points
import cv2

image_path = "plamy.jpg"
password = [0, 1, 2, 3]

if __name__ == "__main__":

	image = cv2.imread(image_path)
	image2 = cv2.imread(image_path)

	img = image_stat.image_stat(image)
	
	image_stat.create_verification_areas()
	
	gaze_data = preproc.preproc()
	gaze_data = map_to_img.map_to_img(img, gaze_data)
	#gaze_data = find_fixations.remove_saccades(gaze_data)
	#print("Gaze data 1: ", gaze_data)
	find_fixations.print_fixations(image2, gaze_data)
	pts = find_fixations.find_fixations(gaze_data)
	print("PTS: ", pts)
	
	find_fixations.print_points(img, pts)
	#verify_points.verify_points(pts, password)
