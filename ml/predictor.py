import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

pollution = pd.read_csv('data/pollution_data.csv')
health = pd.read_csv('data/health_stats.csv')
data = pd.merge(pollution, health, on='Area')

# Features and target
X = data[['AQI', 'PM2.5']]
y = data['Asthma']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('ml/asthma_predictor.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")
