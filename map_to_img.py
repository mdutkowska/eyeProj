import cv2
import preproc as pp

img = cv2.imread("plamy.jpg")

gaze_df = pp.extract_data()

print(coordinates)

for coord in len(gaze_df.index):
	
	coord = tuple(coord)
	print(type(coord))
	cv2.circle(img, (coord), 1, (0, 0, 0), -1)
	
cv2.namedWindow(winname = "Title of Popup Window") 
cv2.imshow("Title of Popup Window", img)

k = cv2.waitKey(0)
