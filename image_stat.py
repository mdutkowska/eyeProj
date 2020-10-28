import cv2
import numpy as np

#thr_y = [0, 465, 920, 1366]
#thr_x = [0, 400, 768]
	
thr_x = list()
thr_y = list()

class verification_area:
	def __init__(self, up, down, left, right):
		self.up=up
		self.down=down
		self.left=left
		self.right=right
	
	def is_in_area(self, x, y):
	
		if (y in range(self.up, self.down)) and (x in range(self.left, self.right)):
			return True
		else:
			return False
			
		
def click_event(event, x, y, flags, params): 

	global thr_x, thr_y
	print(type(thr_x))
	
	# checking for left mouse clicks 
	if event == cv2.EVENT_LBUTTONDOWN: 

		# displaying the coordinates 
		# on the Shell 
		print(x, ' ', y) 

		thr_x.append(x)
		thr_y.append(y)
		
		return x, y	

def mark_areas(img, click_event):


	# displaying the image 
	cv2.imshow('image', img) 

	# setting mouse hadler for the image 
	# and calling the click_event() function 
	cv2.setMouseCallback('image', click_event) 

	# wait for a key to be pressed to exit 
	cv2.waitKey(0) 

	# close the window 
	cv2.destroyAllWindows() 
	
	print(thr_x, "", thr_y)

#TODO PARAMETRIZE THAT
def image_stat(img):
	
	thr_list = list(zip(thr_x, thr_y))
	
	print(thr_list)
	
	for rectangle in range(0, len(thr_list), 2):
	
			print("RECT start ", thr_x[rectangle], thr_y[rectangle])
			print("RECT end ", thr_x[rectangle+1], thr_y[rectangle+1])
			window_name = 'Image'
			start_point = (thr_x[rectangle], thr_y[rectangle]) 
			end_point = (thr_x[rectangle+1], thr_y[rectangle+1]) 
			color = (0, 0, 0) 
			thickness = 2
			  
			img = cv2.rectangle(img, start_point, end_point, color, thickness) 
	
	cv2.namedWindow(winname = "Divsion of image for verification areas. ") 
	img2 = cv2.resize(img, (683, 384))
	cv2.imshow("Divsion of image for verification areas. ", img2)
	
	k = cv2.waitKey(0)
	cv2.imwrite("ver_area.jpg", img)
	return img
	
def create_verification_areas_stat(thr_y = thr_y, thr_x = thr_x):

	i = 0
	for boundry_x in range(len(thr_x)-1):
		for boundry_y in range(len(thr_y)-1):
			if i < areas_number:
				areas_array[i] = verification_area(up = thr_x[boundry_x], down = thr_x[boundry_x+1], left = thr_y[boundry_y], right = thr_y[boundry_y+1])
				i = i + 1
				
	return areas_array
				
def create_verification_areas(thr_y = thr_y, thr_x = thr_x):

	areas_number = int(len(thr_x)/2)
	areas_array = np.empty([areas_number], dtype = verification_area)		

	i = 0
	print(len(thr_x))
	print(len(thr_y))
	for boundry in range(0, len(thr_x)-1, 2):
		
			print("Bx", boundry)
			#if i < areas_number:
			areas_array[i] = verification_area(up = thr_y[boundry], down = thr_y[boundry+1], left = thr_x[boundry], right = thr_x[boundry+1])
			i = i + 1				
	
	print(areas_array[0].__dict__)
	print(areas_array[1].__dict__)
	return areas_array
	
if __name__ == "__main__":
	
	image_stat()
	
	k = cv2.waitKey(0)
