#HackDFW 2019
#Create file with POINT data of different crimes in Dallas area for use in omisci

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

#read in the data
df = pd.read_csv("Police_Incidents.csv")

#points list
coordPoints = []

#for each row
for i in range (df.shape[0]):
    #get the lat and long values
    loc = df["Location1"][i]
    try:
        vals = loc.split("\n")
    except:
        continue
    coordString = vals[-1]

    commaIndex = coordString.find(",")

    try:
        latitude = float(coordString[1:commaIndex])
        longitude = float(coordString[commaIndex+2:-1])
    except:
        continue

    #add point with coordinates to the coordPoints list
    print(latitude)
    print(longitude)
    print("\n")
    coordPoint = Point(longitude, latitude)
    coordPoints.append(coordPoint)

with open('omnisci_points.csv', 'w') as myFile:
    myFile.write("CrimePoints\n")
    for point in coordPoints:
        myFile.write(str(point) + "\n")
myFile.close()

with open('clustering_points.csv', 'w') as myFile2:
    myFile2.write("Longitude,Latitude\n")
    for point in coordPoints:
        myFile2.write(str(point.x) + "," + str(point.y) + "\n")
myFile2.close()

'''
inital attempt at visualization:
geopoints = pd.DataFrame({'Coordinates': coordPoints})
dallas_df = gpd.GeoDataFrame(geopoints, geometry = 'Coordinates')

print(dallas_df.head())

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# We restrict to North America.
ax = world[world.continent == 'North America'].plot(
    color='white', edgecolor='black')

# We can now plot our GeoDataFrame.
dallas_df.plot(ax=ax, color='red')

plt.show()
'''