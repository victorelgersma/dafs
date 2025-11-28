
import pandas as pd

df= pd.read_csv("DAFS_owid_energy_data.csv", delimiter=";")

print(df.describe())
print(df.head(10))

print('columns:')
for i in df.columns:
    print(i)

eu_countries = [
    "Austria","Belgium","Bulgaria","Croatia","Cyprus","Czechia",
    "Denmark","Estonia","Finland","France","Germany","Greece",
    "Hungary","Ireland","Italy","Latvia","Lithuania","Luxembourg",
    "Malta","Netherlands","Poland","Portugal","Romania","Slovakia",
    "Slovenia","Spain","Sweden"
]

EU_DATA = df[df["country"].isin(eu_countries)]

present = set(EU_DATA["country"].unique())
missing = set(eu_countries) - present

print("Present countries:", present)
print("Missing countries:", missing)

print(EU_DATA.describe())

print(EU_DATA.head(15))

columns_share_energy = ["solar_share_energy", "wind_share_energy", "biofuel_share_energy", "nuclear_share_energy", "hydro_share_energy"] 


EU_DATA["renewable_percentage"] = EU_DATA[columns_share_energy].sum()