# Mini Crop Recommendation Project 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# dataset  with almost real world values
data = [
    [90, 40, 50, 25, 80, 6.5, 200, 'rice'],
    [20, 30, 25, 20, 50, 7.0, 100, 'wheat'],
    [60, 35, 40, 24, 65, 6.8, 150, 'maize'],
    [40, 25, 30, 28, 60, 6.9, 90, 'barley'],
    [85, 38, 45, 23, 70, 6.6, 180, 'rice']
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
