from sklearn.cluster import KMeans
import numpy as np
import map_to_img
import matplotlib.pyplot as plt
import cv2
from scipy.spatial import distance 

n_clusters = 4

def remove_saccades(gaze_data, threshold = 30):

	fixations_points = np.empty(0, dtype=int)

	for point in range(len(gaze_data)-1):
		
		dist = distance.euclidean((gaze_data[point, 0], gaze_data[point, 1]),(gaze_data[point+1, 0], gaze_data[point+1, 1]))
		
		if dist < threshold:
			fixations_points = np.append(fixations_points, [point+1])
	
	gaze_data = gaze_data[fixations_points]
	gaze_data = (gaze_data)[(gaze_data)[:, -1].argsort()]
	
	return gaze_data
			
def print_fixations(img, fixation_data):

	fixation_data = np.swapaxes(fixation_data, 0, 1)
	
	gaze_x = fixation_data[0]
	gaze_y = fixation_data[1]
	coord_x_prev, coord_y_prev = gaze_x[0], gaze_y[0]

	cv2.circle(img, (coord_x_prev, coord_y_prev), 3, (0, 0, 0), -1)
		
	for coord in range(1, len(gaze_x)):
		coord_x, coord_y = gaze_x[coord], gaze_y[coord]
		#cv2.line(img, (coord_x_prev, coord_y_prev), (coord_x, coord_y), (0, 0, 0), 2)
		cv2.circle(img, (coord_x, coord_y), 3, (0, 0, 0), -1)
		coord_x_prev, coord_y_prev = coord_x, coord_y
		
	cv2.namedWindow(winname = "Gaze path corrected. ") 
	img2 = cv2.resize(img, (683, 384))
	cv2.imshow("Gaze path corrected. ", img2)

	k = cv2.waitKey(0)

#SPRAWDZI CZY SIE TIMESTAMPY NIE NACHODZA
def find_fixations(gaze_data, n_clusters=4):

	print("Gaze data0 : ", gaze_data)

	gaze_data = remove_saccades(gaze_data)
	

	kmeans = KMeans(n_clusters = n_clusters)

	print("Gaze data2 : ", gaze_data)
	kmeans.fit(gaze_data)
	
	y_km = kmeans.fit_predict(gaze_data)
	
	plt.scatter(gaze_data[y_km == 0,0], gaze_data[y_km == 0,1], s=100, c="red", marker=(5,1))
	plt.scatter(gaze_data[y_km == 1,0], gaze_data[y_km == 1,1], s=100, c="black", marker=(5,1))
	plt.scatter(gaze_data[y_km == 2,0], gaze_data[y_km == 2,1], s=100, c="blue", marker=(5,1))
	plt.scatter(gaze_data[y_km == 3,0], gaze_data[y_km == 3,1], s=100, c="cyan", marker=(5,1))
	
	fixation_points = (kmeans.cluster_centers_)[(kmeans.cluster_centers_)[:, -1].argsort()]
	fixation_points = fixation_points.T
	fixation_points = fixation_points.astype(np.int)
	
	#plt.scatter(fixation_points[0], fixation_points[1], s=100, c="cyan", marker=(5,1))
	#plt.show()
	
	gaze_data = remove_saccades(gaze_data)
	

	kmeans = KMeans(n_clusters = n_clusters)

	print("Gaze data2 : ", gaze_data)
	kmeans.fit(gaze_data)
	
	y_km = kmeans.fit_predict(gaze_data)
	
	plt.scatter(gaze_data[y_km == 0,0], gaze_data[y_km == 0,1], s=100, c="red", marker=(5,1))
	plt.scatter(gaze_data[y_km == 1,0], gaze_data[y_km == 1,1], s=100, c="black", marker=(5,1))
	plt.scatter(gaze_data[y_km == 2,0], gaze_data[y_km == 2,1], s=100, c="blue", marker=(5,1))
	plt.scatter(gaze_data[y_km == 3,0], gaze_data[y_km == 3,1], s=100, c="cyan", marker=(5,1))
	
	fixation_points = (kmeans.cluster_centers_)[(kmeans.cluster_centers_)[:, -1].argsort()]
	fixation_points = fixation_points.T
	fixation_points = fixation_points.astype(np.int)
	
	#plt.scatter(fixation_points[0], fixation_points[1], s=100, c="cyan", marker=(5,1))
	#plt.show()
	
	gaze_data = remove_saccades(gaze_data)
	

	kmeans = KMeans(n_clusters = n_clusters)

	print("Gaze data2 : ", gaze_data)
	kmeans.fit(gaze_data)
	
	y_km = kmeans.fit_predict(gaze_data)
	
	plt.scatter(gaze_data[y_km == 0,0], gaze_data[y_km == 0,1], s=100, c="red", marker=(5,1))
	plt.scatter(gaze_data[y_km == 1,0], gaze_data[y_km == 1,1], s=100, c="black", marker=(5,1))
	plt.scatter(gaze_data[y_km == 2,0], gaze_data[y_km == 2,1], s=100, c="blue", marker=(5,1))
	plt.scatter(gaze_data[y_km == 3,0], gaze_data[y_km == 3,1], s=100, c="cyan", marker=(5,1))
	
	fixation_points = (kmeans.cluster_centers_)[(kmeans.cluster_centers_)[:, -1].argsort()]
	fixation_points = fixation_points.T
	fixation_points = fixation_points.astype(np.int)
	
	#plt.scatter(fixation_points[0], fixation_points[1], s=100, c="cyan", marker=(5,1))
	#plt.show()
	
	gaze_data = remove_saccades(gaze_data)
	

	kmeans = KMeans(n_clusters = n_clusters)

	print("Gaze data2 : ", gaze_data)
	kmeans.fit(gaze_data)
	
	y_km = kmeans.fit_predict(gaze_data)
	
	plt.scatter(gaze_data[y_km == 0,0], gaze_data[y_km == 0,1], s=100, c="red", marker=(5,1))
	plt.scatter(gaze_data[y_km == 1,0], gaze_data[y_km == 1,1], s=100, c="black", marker=(5,1))
	plt.scatter(gaze_data[y_km == 2,0], gaze_data[y_km == 2,1], s=100, c="blue", marker=(5,1))
	plt.scatter(gaze_data[y_km == 3,0], gaze_data[y_km == 3,1], s=100, c="cyan", marker=(5,1))
	
	fixation_points = (kmeans.cluster_centers_)[(kmeans.cluster_centers_)[:, -1].argsort()]
	fixation_points = fixation_points.T
	fixation_points = fixation_points.astype(np.int)
	
	#plt.scatter(fixation_points[0], fixation_points[1], s=100, c="cyan", marker=(5,1))
	#plt.show()
	
	
	
	return fixation_points
	
def print_points(img, points):

	points_x = np.array(points[0], dtype = int)
	points_y = np.array(points[1], dtype = int)
	
	print("X ", points_x)
	print("Y ", points_y)

	for point in range(len(points_x)):
		cv2.rectangle(img, (points_x[point], points_y[point]), ((points_x[point]+15), (points_y[point]+15)), (0, 255, 0), -1)
		
	img2 = cv2.resize(img, (683, 384))
	cv2.imshow("winname", img2)
	k = cv2.waitKey(0)
		
	cv2.imwrite("ver_points.jpg", img)
		
if __name__ == "__main__":
	find_fixations();
	k = cv2.waitKey(0)
