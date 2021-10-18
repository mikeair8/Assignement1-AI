import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv("RIKTIG DATA SET0.1.csv")

#1.1 Identify 5 unique features from this data set.

#TurID
#Fullt_tog
#Antall_Plasser_igjen
#Kjøretøy_Kapasitet
#Pasasjerer_Ombord,




#1.2 Apply feature engineering on them in Python.

#Some values in the last column were negative even though thats not possible con
#therefore i did some feature engineering to just change the value from -x to x
kolonne1 = data["Passasjerer_Ombord,"]
for i in range (len(data["Passasjerer_Ombord,"])):
    if kolonne1[i] < 0:
        kolonne1[i]=kolonne1[i]*-1

#there were around 50 cells in column L that were empty so i just filled them with the most frequent value
#the 50 cells in question were filled with ":" so i just deleted them all directly in excel to make it easier
data["Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra"].fillna(data["Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra"].mode()[0], inplace = True)

#i made a new unique feature that shows how many seats are left
data["Antall_Plasser_igjen"] = data["Kjøretøy_Kapasitet"] - data["Passasjerer_Ombord,"]

#this new feature will tell us if the train is full or not
data["Fullt_tog"] = data["Antall_Plasser_igjen"] == 0



#1.3 Visualize each feature in the form of a graph using python libraries.

#there are only to features in our data set that only contain numeric values and therefore these are the only ones we can plot
data = pd.DataFrame(data, dtype='object')
axs = data.plot(subplots=True, figsize=(30, 30));
plt.delaxes(axs[0])