import numpy as np
import pandas as pd

red_df=pd.read_csv("C:\\Users\\Asus\\.spyder-py3\\winequality\\winequality-red.csv",sep=";")
white_df=pd.read_csv("C:\\Users\\Asus\\.spyder-py3\\winequality\\winequality-white.csv",sep=";")

print(red_df.head())
red_df.rename(columns={"total sulfur dioxide":"total sulfur_dioxide"})
red_df.info()
color_red=np.repeat("red",red_df.shape[0])
red_df["color"]=color_red
print(red_df.head())
print()
print()
wine_df=red_df.append(white_df,sort=False)
print(wine_df.head())
wine_df.to_csv("new_wine.csv",index=False)

print(wine_df.groupby("color").mean()