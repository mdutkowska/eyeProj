import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

txt_file = open("ScreenRecorderPath.txt", "r+")

eye_x = np.empty(1)
eye_y = np.empty(1)

timestamp = np.empty(1)

mouse_x = np.empty(1)
mouse_y = np.empty(1)

idx = np.empty(1)
theme_change = 0
theme_change_idx = np.empty(1)

for line in txt_file.readlines():

	print(line)
	if "ImageFile:" in line:
		print("Reading a file started. ")
	else:

		splited = line.split(" ")
		
		eye_x = np.append(eye_x, float(splited[0]))
		eye_y = np.append(eye_y, float(splited[1]))
		
		timestamp = np.append(timestamp, int(splited[2]))

		mouse_x = np.append(mouse_x, float(splited[4]))
		mouse_y = np.append(mouse_y, float(splited[5]))
		
		idx = np.append(idx, int(sptiled[6]))
		
		if int(splited[7]) is not(theme_change):
			theme_change_idx = np.append(theme_change_idx, 1)
			theme_change = not(theme_change)
		else:
			theme_change_idx = np.append(theme_change_idx, 0)
			theme_change = theme_change

print(np.size(eye_x))
print(eye_x)

eye_y = -(eye_y)

eyes = np.vstack((eye_x[1:], eye_y[1:]))
df_eyes = pd.DataFrame.from_records(eyes.T, columns = ["eye_x", "eye_y"])

print(df_eyes.count())
df_eyes.plot.scatter(x="eye_x", y="eye_y")
plt.show()
#sns.set_theme()
#sns.scatterplot(data=eyes)
#plt.show()
