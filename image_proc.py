import cv2

x1, x2, y1, y2 = 0, 0, 0, 0

img = cv2.imread("plamy.jpg")

def draw_rect(event, x, y, flags, param):

	global ix, iy, drawing, img
	
	if event == cv2.EVENT_LBUTTONDOWN:
		print("CLICK")
		drawing = True
		ix = x
		iy = y
		
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.rectangle(img, pt1=(ix, yx), 
					pt = (x, y), color =(255, 0, 0), thickness =-1)
			
	elif event == cv2.EVENT_LBUTTONUP:
		drawing ==False
		cv2.rectangle(img, pt1 =(ix, iy), 
				pt2 =(x, y), color =(255, 0, 0), thickness =-1)
		
cv2.namedWindow(winname = "Mark points. ")
cv2.setMouseCallback("Mark points, ", draw_rect)

while True:
	cv2.imshow("Mark points. ", img)
	
	if cv2.waitKey(0) == 27:
		break

cv2.destroyAllWindows()
