import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [15.50, 6.501] # Canvas Area
plt.rcParams["figure.autolayout"] = True
phones_data = pd.read_csv('/content/Best_Selling_Mobile_Phones_2020.csv') # Define your own path
headers = ['phone','company','sold']
phones_data.set_index('Phone').plot()
plt.show()
