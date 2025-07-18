from flask import Flask, render_template
import pandas as pd
import folium
import pickle
from geopy.distance import geodesic

model = pickle.load(open('ml/asthma_predictor.pkl', 'rb'))

app = Flask(__name__)

def is_underserved(area_lat, area_lon, facilities_df, max_dist_km=3):
    for _, row in facilities_df.iterrows():
        if row['Type'] == 'EMF-Free':
            dist = geodesic((area_lat, area_lon), (row['Latitude'], row['Longitude'])).km
            if dist <= max_dist_km:
                return False
    return True

@app.route('/')
def map_view():
    # Load data
    pollution = pd.read_csv('data/pollution_data.csv')
    facilities = pd.read_csv('data/facilities.csv')

    # Create base map
    m = folium.Map(location=[17.3850, 78.4867], zoom_start=13)

    # Add pollution markers with asthma prediction
    for _, row in pollution.iterrows():
        predicted_asthma = model.predict([[row['AQI'], row['PM2.5']]])[0]
        underserved = is_underserved(row['Latitude'], row['Longitude'], facilities)
        status = "❗Underserved" if underserved else "✅ Covered"

        color = 'green' if row['AQI'] < 100 else 'orange' if row['AQI'] < 200 else 'red'

        popup_text = (
            f"<b>{row['Area']}</b><br>"
            f"AQI: {row['AQI']}<br>"
            f"PM2.5: {row['PM2.5']}<br>"
            f"Predicted Asthma: {predicted_asthma:.1f}%<br>"
            f"<b>{status}</b>"
        )

        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=10,
            popup=popup_text,
            color=color,
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    # Add existing facility markers
    for _, row in facilities.iterrows():
        icon_color = 'blue' if row['Type'] == 'EMF-Free' else 'gray'
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Name']} ({row['Type']})",
            icon=folium.Icon(color=icon_color)
        ).add_to(m)

    # --- Recommended facility from Day 3 ---
    recommended_lat = 16.3424
    recommended_lon = 78.8820

    folium.Marker(
        [recommended_lat, recommended_lon],
        popup="📍 Recommended EMF-Free Facility",
        icon=folium.Icon(color='white', icon='plus-sign', prefix='glyphicon')
    ).add_to(m)

    # Render map in template
    return render_template('map.html', folium_map=m._repr_html_())

if __name__ == '__main__':
    app.run(debug=True)
