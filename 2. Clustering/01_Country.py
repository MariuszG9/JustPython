import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data = pd. read_csv('Country clusters.csv')

# PLOT the data
plt.scatter(data['Longitude'],data['Latitude'])
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show

# Select the features
x = data.iloc[:,1:3]

# Clustering
kmeans = KMeans(3)
kmeans.fit(x)

#Clustering results
identified_clusters = kmeans.fit_predict(x)
identified_clusters

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters

# PLOT the data_new
plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],c=data_with_clusters['Cluster'],cmap='plasma')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show
