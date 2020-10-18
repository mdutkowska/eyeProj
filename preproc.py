import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def extract_data(log_path="ScreenRecorderPath.txt"):

	txt_file = open(log_path, "r+")

	gaze_df = pd.DataFrame(columns = ["gaze_x", "gaze_y", "timestamp", "mouse_x", "mouse_y", "is_theme_changed"])

	theme_change_prev = 0

	for line in txt_file.readlines():

		print(line)
		if "ImageFile:" in line:
			print("Extracting data from file started. ")
		else:

			splited = line.split(" ")
			
			eye_x = float(splited[0])
			eye_y = -(float(splited[1]))+1
			
			timestamp = int(splited[2])

			mouse_x = float(splited[4])
			mouse_y = float(splited[5])
			
			theme_change = int(splited[7])
			
			if theme_change is not(theme_change_prev):
				is_theme_change = True
				theme_change_prev = theme_change
			else:
				is_theme_change = False
				theme_change_prev = theme_change

			gaze_df = gaze_df.append({"gaze_x": eye_x, "gaze_y": eye_y, "timestamp": timestamp, "mouse_x": mouse_x, "mouse_y": mouse_y, "is_theme_changed": is_theme_change}, ignore_index = True)

	print("DataFrame contents: \n", gaze_df, "sep=\n")
	
	print(gaze_df.count())
	
	#gaze_df.plot.scatter(x = "gaze_x", y = "gaze_y")
	#plt.show()
	
	gaze_df.drop(gaze_df[gaze_df["gaze_x"] > 1].index, inplace=True)
	gaze_df.drop(gaze_df[gaze_df["gaze_y"] > 1].index, inplace=True)
	gaze_df.drop(gaze_df[gaze_df["gaze_x"] < 0].index, inplace=True)
	gaze_df.drop(gaze_df[gaze_df["gaze_y"] < 0].index, inplace=True)
	
	gaze_df = gaze_df.reset_index()
	
	print(gaze_df.count())
	
	#gaze_df.plot.scatter(x = "gaze_x", y = "gaze_y")
	#plt.show()
	
	print("Extracting data finished. ")
	
	return gaze_df
	
if __name__ == "__main__":
	extract_data()
