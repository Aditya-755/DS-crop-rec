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

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)
#for alternate crops
ideal_conditions = {
    'rice': {'N': 87, 'P': 39, 'K': 47}, 'wheat': {'N': 20, 'P': 30, 'K': 25},
    'maize': {'N': 60, 'P': 35, 'K': 40}, 'barley': {'N': 40, 'P': 25, 'K': 30},
    'mango': {'N': 20, 'P': 30, 'K': 32}, 'grapes': {'N': 18, 'P': 25, 'K': 28},
    'apple': {'N': 10, 'P': 15, 'K': 12}, 'orange': {'N': 22, 'P': 18, 'K': 10},
    'papaya': {'N': 95, 'P': 55, 'K': 50}, 'chickpea': {'N': 20, 'P': 65, 'K': 20},
    'kidneybean': {'N': 20, 'P': 68, 'K': 19}, 'pigeonpea': {'N': 18, 'P': 60, 'K': 22},
    'jute': {'N': 120, 'P': 42, 'K': 40}, 'cotton': {'N': 100, 'P': 40, 'K': 38},
    'sugarcane': {'N': 110, 'P': 55, 'K': 50}
}

fertilizer_suggestions = {
    'N': 'Urea', 'P': 'DAP (Di-Ammonium Phosphate)', 'K': 'MOP (Muriate of Potash)'
}


print("Enter soil and weather values to get crop recommendation:")
N = float(input("Nitrogen (N, kg/ha approx): "))
P = float(input("Phosphorus (P, kg/ha approx): "))
K = float(input("Potassium (K, kg/ha approx): "))
temp = float(input("Temperature (°C): "))
humidity = float(input("Humidity (%): "))
ph = float(input("pH level: "))
rainfall = float(input("Rainfall (mm): "))
new_input_data=[[N,P,K,temp, humidity,ph,rainfall,]]
prediction=model.predict(new_input_data)
print("-" * 40)
print(f"Top Recommendation: '{prediction[0].title()}' is the best match for your current soil.")
print("-" * 40)

# Alternative Crop Suggestions 
threshold = 0.75
alternatives = []

for crop, ideals in ideal_conditions.items():
    if crop == prediction[0]:
        continue

    is_close_enough = (
        N >= ideals['N'] * threshold and
        P >= ideals['P'] * threshold and
        K >= ideals['K'] * threshold
    )

    if is_close_enough:
        deficits = {}
        if N < ideals['N']: deficits['N'] = ideals['N'] - N
        if P < ideals['P']: deficits['P'] = ideals['P'] - P
        if K < ideals['K']: deficits['K'] = ideals['K'] - K

        if deficits:
            alternatives.append({'crop': crop, 'deficits': deficits})

if alternatives:
    print("\n💡 Alternative Crop Options with Soil Correction:")
    for alt in alternatives:
        print(f"\n* You can also grow: {alt['crop'].title()}")
        for nutrient, deficit in alt['deficits'].items():
            fertilizer = fertilizer_suggestions[nutrient]
            if nutrient == 'N': fertilizer_amount = deficit / 0.46
            elif nutrient == 'P': fertilizer_amount = deficit / 0.46
            else: fertilizer_amount = deficit / 0.60

            print(f"  - Action: Your soil is low in {nutrient} by {deficit:.1f} units.")
            print(f"  - Suggestion: Add approx. {fertilizer_amount:.1f} kg/ha of {fertilizer}.")
else:
    print("\nNo other suitable alternative crops found within a manageable range.")
