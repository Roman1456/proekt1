import pandas as pd

df = pd.read_csv('Space_Corrected (1).csv')
df.info()

df[" Rocket "]=df[' Rocket '].fillna(0)
df[" Rocket "]= pd.to_numeric(df[" Rocket "], errors='coerce' )
print(df['Rocket'].max())