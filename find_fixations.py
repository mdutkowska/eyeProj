from sklearn.cluster import KMeans
import map_to_img
import matplotlib.pyplot as plt
import cv2

n_clusters = 4

kmeans = KMeans(n_clusters = n_clusters)
gaze_data = map_to_img.map_to_img()

kmeans.fit(gaze_data)

print(kmeans.cluster_centers_)
y_km = kmeans.fit_predict(gaze_data)

plt.scatter(gaze_data[y_km == 0,0], gaze_data[y_km == 0,1], s=100, c="red", marker=(5,1))
plt.scatter(gaze_data[y_km == 1,0], gaze_data[y_km == 1,1], s=100, c="black", marker=(5,1))
plt.scatter(gaze_data[y_km == 2,0], gaze_data[y_km == 2,1], s=100, c="blue", marker=(5,1))
plt.scatter(gaze_data[y_km == 3,0], gaze_data[y_km == 3,1], s=100, c="cyan", marker=(5,1))

plt.show()

k = cv2.waitKey(0)
