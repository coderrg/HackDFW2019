#import necessary libraries
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from shapely.geometry import Point, Polygon

#read in all the crime location data points
crimes = pd.read_csv("clustering_points.csv")

#get rid of the outliers
badIndexes = [19073, 26939, 50300, 102603, 124110, 227991, 235297, 284801, 333121, 358173, 369179, 416050, 447407, 485519]

#we obtained the above outliers with the code below
'''
count = 0
for i in range (crimes.shape[0]):
    if (crimes.iloc[i]['Longitude'] <= -98 or crimes.iloc[i]['Longitude'] >= -95 or crimes.iloc[i]['Latitude'] <= 31 or crimes.iloc[i]['Latitude'] >= 34):
        badIndexes.append(i)
    print(i)

print(badIndexes)
'''
crimes.drop(crimes.index[badIndexes])

#make the ML model
kmeans = KMeans(n_clusters = 6, verbose = 2)

#fit the model 
predictions = kmeans.fit_predict(crimes)

#get the cluster centers
centers = kmeans.cluster_centers_

#turn centers into Points
coordPoints = []
for i in range (len(centers)):
    centerPoint = Point(centers[i][0], centers[i][1])
    #make sure it is reasonable
    if (centerPoint.x <= -90):
        coordPoints.append(centerPoint)

#write the Points in a file
with open('omnisci_centers.csv', 'w') as myFile:
    myFile.write("CrimeCenters\n")
    for point in coordPoints:
        myFile.write(str(point) + "\n")
myFile.close()