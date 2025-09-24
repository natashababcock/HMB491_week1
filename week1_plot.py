import pandas as pd
import matplotlib.pyplot as plt

# TODO: load the dataset as pandas dataframe
df_teeth = pd.read_csv("/Users/natashababcock/Documents/HMB491_modules/HMB491_week1/mammal_teeth.csv")

plt.figure(figsize=(12, 15)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(True)

# TODO: change the title name to include your name
plt.title("Natasha's plot for mammal_teeth dataset")
plt.savefig("natasha_mammal_teeth_scatterplot.png", dpi=150) # save the figure