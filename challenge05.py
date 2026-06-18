import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
data = pd.read_csv(url)

array = data.to_numpy()
print(array.shape)


#Welche Spalte ist der Glukosewert?
print(data.head())

#Finde alle Patienten mit Glukose > 140
high_glucose = array[:,1] > 140

  #oder

hoher_zucker = np.where(array[:,1] > 140)

#Berechne Durchschnitts-Glukose dieser Gruppe

mean_sugar = np.mean(array[:,1])

#Finde Anteil der Patienten mit Outcome = 1
outcome = array[:,8] == 1
print(sum(outcome)/len(array)*100)

#Baue einen einfachen Risiko-Score:
#Glukose > 140 → +1
high_glucose = array[:,1] > 140
#BMI > 30 → +1
high_bmi = array[:,5] > 30
#Alter > 50 → +1
high_age = array[:, 7] > 50

score = high_glucose.astype(int) + high_bmi.astype(int) + high_age.astype(int)

scores = np.zeros(768).reshape(-1,1)
array = np.hstack((array, scores))

array[:,9] = score

def risk_class(score):
    if score <= 1:
        return "low"
    elif score == 2:
        return "medium"
    else:
        return "high"

risk_classes = [risk_class(s) for s in array[:,9]]
array = np.hstack((array, np.array(risk_classes).reshape(-1,1)))

print(array)