import image_stat
import preproc
import map_to_img
import find_fixations
import cv2

image = "plamy.jpg"

if __name__ == "__main__":

	img = cv2.imread(image)

	img = image_stat.image_stat(img)
	gaze_data = preproc.preproc()
	gaze_data = map_to_img.map_to_img(img, gaze_data)
	pts = find_fixations.find_fixations(gaze_data)
	
