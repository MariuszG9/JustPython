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
data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters

# PLOT the data_new
plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],c=data_with_clusters['Cluster'],cmap='plasma')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show

kmeans.inertia_
WCSS = []

for i in range(1,7):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss_iter = kmeans.inertia_
    WCSS.append(wcss_iter)

number_clusters = range(1,7)
plt.plot(number_clusters,WCSS)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Within-cluster Sum of Squares')
