🌍 EnvJustice – Environmental Justice Data Platform

**EnvJustice** is a map-based platform that uses pollution and health data to promote fair access to clean environments and healthcare. It combines environmental monitoring, machine learning, and geospatial tools to:

- 🔍 Predict asthma risk based on AQI and PM2.5
- 🏥 Identify underserved regions without EMF-Free facilities
- 📍 Recommend optimal new locations for healthcare centers



🚀 Features

- 🗺️ Interactive map displaying AQI, PM2.5, and asthma risk
- 🤖 ML-powered asthma prediction using pollution + health data
- 📉 Highlights underserved areas using real facility data
- 🧭 Recommends new EMF-Free healthcare locations using clustering
- 🧪 Uses health statistics to improve area vulnerability analysis


 📂 Project Structure

envjustice/
├── app.py                      # Main Flask application
├── ml/
│   ├── asthma_model.py         # Trains asthma prediction model
│   ├── recommend_facilities.py # Uses clustering to suggest new facilities
│   └── asthma_predictor.pkl    # Saved model file
├── data/
│   ├── pollution_data.csv      # AQI and PM2.5 values
│   ├── health_stats.csv        # Population & asthma statistics
│   └── facilities.csv          # Existing facility locations
├── templates/
│   └── map.html                # Folium map rendering
├── static/
│   └── (optional CSS/assets)
├── requirements.txt
└── README.md
