import pandas as pd

# Use the following dataframe:
data = {
    "Region": ["A", "B", "A", "C", "B", "C", "A"],
    "EnergyUsage": [10, 20, 30, 40, 50, 60, 70],
    "Sustainable": [True, False, True, False, True, False, True]
}

df = pd.DataFrame(data)

print(df)

rows = []
for index,row in df.iterrows():
    if (row["Sustainable"] == True and row["EnergyUsage"] > 20):
       rows.append(row)

print(pd.DataFrame(rows))



CumulativeEnergyUsage = 0 
rows2= []
i = 0
while CumulativeEnergyUsage < 50: 
    current_row = df.iloc[i]
    if (current_row["Sustainable"] == True):
        rows2.append(current_row)
        CumulativeEnergyUsage = CumulativeEnergyUsage + current_row["EnergyUsage"]
    print(f"Total energy usage {CumulativeEnergyUsage}")
    print("rows contributing")
    print(pd.DataFrame(rows2))
    i = i+1



