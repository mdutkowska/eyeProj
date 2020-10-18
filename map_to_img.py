import numpy as np
import cv2
import preproc as pp

res_x = 1366
res_y = 768


#PODZIELIC NA DWIE FUNKCJE
def map_to_img(res_x = 1366, res_y = 768):

	img = cv2.imread("plamy.jpg")

	gaze_df = pp.extract_data()
	
	gaze_x = gaze_df["gaze_x"]*res_x
	gaze_y = gaze_df["gaze_y"]*res_y
	timestamp = gaze_df["timestamp"]

	pixels_coord = np.array([gaze_x, gaze_y, timestamp])
	pixels_coord = pixels_coord.T
	
	coord_x, coord_y = int(gaze_x[0]), int(gaze_y[0])	
	coord_x_prev, coord_y_prev = coord_x, coord_y
	
	cv2.circle(img, (coord_x, coord_y), 3, (0, 0, 0), -1)
		
	for coord in range(1, len(gaze_df.index)):
		coord_x, coord_y = int(gaze_x[coord]), int(gaze_y[coord])
		cv2.line(img, (coord_x_prev, coord_y_prev), (coord_x, coord_y), (0, 0, 0), 2)
		coord_x_prev, coord_y_prev = coord_x, coord_y
		
	cv2.namedWindow(winname = "Title of Popup Window") 
	cv2.imshow("Title of Popup Window", img)

	return pixels_coord
	
if __name__ == "__main__":

	print((map_to_img(res_x = 1366, res_y = 768))[0])
	
	k = cv2.waitKey(0)
