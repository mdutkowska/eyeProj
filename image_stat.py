import cv2
import numpy as np

thr_y = [0, 465, 920, 1366]
thr_x = [0, 400, 768]

def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)

class verification_area:
	def __init__(self, up, down, right, left):
		self.up=up
		self.down=down
		self.right=right
		self.left=left
	#TODO
	def is_in_area():
		pass
		
areas_number = (len(thr_y)-1)*(len(thr_x)-1)
areas_array = np.empty([areas_number], dtype = verification_area)

#TODO PARAMETRIZE THAT
def image_stat(img, thr_y1 = thr_y[1], thr_y2 = thr_y[2], thr_x1 = thr_x[1]):

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
	
	#cv2.namedWindow(winname = "Title of Popup Window") 
	#cv2.imshow("Title of Popup Window", img)
	return img
	
def create_verification_areas(thr_y = thr_y, thr_x = thr_x):

	i = 0
	#TODO
	for prev_y, boundry_y, next_y in neighborhood(thr_y):
		for prev_x, boundry_x, next_x in neighborhood(thr_x):
			if i < areas_number:
				print(boundry_x)
				areas_array[i] = verification_area(prev_x, boundry_x, prev_y, boundry_y)
				i = i + 1
		

if __name__ == "__main__":
	
	create_verification_areas()
	
	print(areas_array[0].__dict__)
	print(areas_array[1].__dict__)
	print(areas_array[5].__dict__)
	
	k = cv2.waitKey(0)
