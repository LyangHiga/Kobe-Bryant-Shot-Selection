import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(d):
	d.hist(bins=50, figsize=(20,15))
	plt.savefig("attribute_histogram_plots")
	plt.show()

def plot_scatter_matrix(d, atr):
	sns.pairplot(d, vars=atr, hue="shot_made_flag", height=2)
	plt.savefig("scatter_matrix_plot")
	plt.show()

data = pd.read_csv("data.csv")
#training set
kobe = data[data["shot_made_flag"].notnull()].reset_index()

#print(data.head())
#print(data.info())
#print(data.describe())
print(kobe.head())
print(kobe.info())
print(kobe.describe())
print(kobe.describe(include=["object", "category"]))
print(kobe.shape)

#plot_hist(kobe)
attributes = ["loc_x", "loc_y", "lat", "lon", "shot_distance"]
#plot_scatter_matrix(kobe, attributes)


#lets look to correlations
corr_matrix = kobe.corr()
for a in attributes:
	print("*****"+ a+"******")
	print(corr_matrix[a].sort_values(ascending = False))
#As we can see both in scatter plot and corr_matrix	"loc_x", "loc_y", "lat", "lon" represent the same thing

print(corr_matrix["shot_made_flag"].sort_values(ascending=False))

target = kobe["shot_made_flag"].copy()
kobe.set_index('shot_id', inplace=True)

kobe = kobe.drop("index",axis=1)
kobe = kobe.drop("shot_made_flag",axis=1)
kobe = kobe.drop("lat",axis=1)
kobe = kobe.drop("lon",axis=1)
kobe = kobe.drop("team_id",axis=1)
kobe = kobe.drop("team_name",axis=1)
kobe = kobe.drop("game_id",axis=1)
kobe = kobe.drop("game_event_id",axis=1)

print(kobe.head())
print(kobe.info())
print(kobe.describe())
print(kobe.describe(include=["object", "category"]))




