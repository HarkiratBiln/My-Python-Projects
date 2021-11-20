from os import sep
import pandas as pd
import plotly.express as px

df  = pd.read_csv("data_cases.csv",sep = "\t")
print (df.head())
fig = px.scatter(df, x = "date", y = "cases", color = "country")

fig.show()