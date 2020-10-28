import image_stat
import preproc
import map_to_img
import find_fixations
import verify_points
import cv2

image_path = "plamy.jpg"
password = [0, 1, 4, 5]

if __name__ == "__main__":

	image = cv2.imread(image_path)
	image2 = cv2.imread(image_path)

	image_stat.mark_areas(image, image_stat.click_event)
	img = image_stat.image_stat(image)
	
	areas = image_stat.create_verification_areas()
	
	#gaze_data = preproc.preproc()
	#gaze_data = map_to_img.map_to_img(img, gaze_data)
	
	#find_fixations.print_fixations(image2, gaze_data)
	#pts = find_fixations.find_fixations(gaze_data)
	
	#find_fixations.print_points(image2, pts)
	#verify_points.verify_points(pts, areas)
