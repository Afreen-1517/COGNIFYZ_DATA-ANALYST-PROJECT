import pandas as pd
df = pd.read_csv("dataset.csv")
# Fill missing cuisines based on city mode
df["Cuisines"] = df.groupby("City")["Cuisines"].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else "UNKNOWN"))
# Rename columns for easy use
df.columns = df.columns.str.lower().str.replace(" ", "_")

"""" TASK3 : Geographic Analysis
Plot the locations of restaurants on a map using longitude and latitude coordinates.
Identify any patterns or clusters of restaurants in specific areas."""


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

coords = df[['latitude', 'longitude']].dropna()

kmeans = KMeans(n_clusters=5, random_state=42)
coords['Cluster'] = kmeans.fit_predict(coords)

coords['city'] = df.loc[coords.index, 'city']

print("\nCluster represents these cities:")
print(coords.groupby('Cluster')['city'].agg(lambda x: x.mode()[0]))

plt.scatter(coords['longitude'], coords['latitude'], c=coords['Cluster'])
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Clusters of Restaurants")
plt.show()
