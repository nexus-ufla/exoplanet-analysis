from src.data_fetch import fetch_exoplanet_data

df = fetch_exoplanet_data()
print(df.head())