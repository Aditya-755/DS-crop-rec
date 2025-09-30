# Mini Crop Recommendation Project 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# dataset  with almost real world values
data = [
    [90, 40, 50, 25, 80, 6.5, 200, 'rice'],
    [20, 30, 25, 20, 50, 7.0, 100, 'wheat'],
    [60, 35, 40, 24, 65, 6.8, 150, 'maize'],
    [40, 25, 30, 28, 60, 6.9, 90, 'barley'],
    [85, 38, 45, 23, 70, 6.6, 180, 'rice'],
    [20, 30, 32, 33, 52, 6.4, 95, 'mango'],
    [18, 25, 28, 26, 92, 7.2, 105, 'grapes'],
    [10, 15, 12, 14, 90, 6.1, 115, 'apple'],
    [22, 18, 10, 25, 95, 6.8, 75, 'orange'],
    [95, 55, 50, 25, 98, 6.5, 250, 'papaya'],
    [20, 65, 20, 20, 82, 5.8, 180, 'chickpea'],
    [20, 68, 19, 28, 55, 5.5, 88, 'kidneybean'],
    [18, 60, 22, 29, 60, 6.8, 110, 'pigeonpea'] ,
    [120, 42, 40, 24, 78, 6.9, 850, 'jute'],
    [100, 40, 38, 25, 80, 5.9, 200, 'cotton'],
    [110, 55, 50, 28, 85, 6.0, 1200, 'sugarcane'] 
]

# Column names
columns = ['N', 'P', 'K', 'Temperature', 'Humidity', 'pH', 'Rainfall', 'Crop']
df = pd.DataFrame(data, columns=columns)

X = df.drop('Crop', axis=1)
y = df['Crop']

# Training part
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

print("Enter soil and weather values to get crop recommendation:")
N = float(input("Nitrogen (N, kg/ha approx): "))
P = float(input("Phosphorus (P, kg/ha approx): "))
K = float(input("Potassium (K, kg/ha approx): "))
temp = float(input("Temperature (°C): "))
humidity = float(input("Humidity (%): "))
ph = float(input("pH level: "))
rainfall = float(input("Rainfall (mm): "))
#predict
new_input_data = [[N, P, K, temp, humidity, ph, rainfall]]
new_input_df = pd.DataFrame(new_input_data, columns=X.columns)

prediction = model.predict(new_input_df)
print(f"\nInput conditions: {new_input_data[0]}")
print(f"Recommended Crop for these conditions will be: {prediction[0]}")
