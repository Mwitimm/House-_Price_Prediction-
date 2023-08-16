import pandas as pd


path= "Data/rent_apts.csv"

data =  pd.read_csv(path)

print(data.head(5))

