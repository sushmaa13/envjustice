import pandas as pd
from sklearn.cluster import KMeans
import folium

# Load data
pollution = pd.read_csv('data/pollution_data.csv')
facilities = pd.read_csv('data/facilities.csv')

# Identify underserved areas (no EMF-Free within 3km)
from geopy.distance import geodesic

def is_underserved(lat, lon):
    for _, row in facilities.iterrows():
        if row['Type'] == 'EMF-Free':
            dist = geodesic((lat, lon), (row['Latitude'], row['Longitude'])).km
            if dist <= 3:
                return False
    return True

underserved = []
for _, row in pollution.iterrows():
    if is_underserved(row['Latitude'], row['Longitude']):
        underserved.append((row['Latitude'], row['Longitude']))

# Apply KMeans to find 2 best new locations
if underserved:
    kmeans = KMeans(n_clusters=1, random_state=42)
    kmeans.fit(underserved)
    new_locations = kmeans.cluster_centers_

    # Print recommendations
    print("📍 Suggested new EMF-Free facility locations:")
    for i, loc in enumerate(new_locations, 1):
        print(f"{i}. Latitude: {loc[0]:.4f}, Longitude: {loc[1]:.4f}")
else:
    print("✅ All areas are already covered!")
