import cv2

thr_y1 = 465
thr_y2 = 920

thr_x1 = 400


#TODO PARAMETRIZE THAT
def set_static_boundries(thr_y1, thr_y2, thr_x1):

	img = cv2.imread("plamy.jpg")

	window_name = 'Image'
	start_point = (thr_y1, 0) 
	end_point = (thr_y1, 768) 
	color = (0, 0, 0) 
	thickness = 2
	  
	img = cv2.line(img, start_point, end_point, color, thickness) 

	window_name = 'Image'
	start_point = (thr_y2, 0) 
	end_point = (thr_y2, 768) 
	color = (0, 0, 0) 
	thickness = 2
	  
	img = cv2.line(img, start_point, end_point, color, thickness) 

	window_name = 'Image'
	start_point = (0, thr_x1) 
	end_point = (1366, thr_x1) 
	color = (0, 0, 0) 
	thickness = 2
	  
	img = cv2.line(img, start_point, end_point, color, thickness) 
	
	cv2.namedWindow(winname = "Title of Popup Window") 
	cv2.imshow("Title of Popup Window", img)

if __name__ == "__main__":
	set_static_boundries(thr_y1, thr_y2, thr_x1)

	k = cv2.waitKey(0)
