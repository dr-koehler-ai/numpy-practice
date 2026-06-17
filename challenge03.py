import numpy as np

#100 Patienten mit zufälligen: Herzfrequenzen, Blutdrücken, Laktatwerten
rr_heart_rate = np.random.randint(0, 200, size=(100, 2))
lac = np.random.randint(0, 20, size=(100,1))
criteria = np.zeros((100,1))
patients = np.hstack((rr_heart_rate, lac, criteria))
#print(patients)

#Wie viele Patienten haben Tachykardie?
def tachykardie(arr):
  tachykardie = np.array([])
  for i in range(len(arr)):
    if arr[i][0] > 100:
      tachykardie = np.append(tachykardie, arr[i][0])
  return tachykardie
print(len(tachykardie(patients)))

#Wie viele Patienten haben Hypotonie?
def hypotonie(arr):
  hypotonie = np.array([])
  for i in range(len(arr)):
    if arr[i][1] < 90:
      hypotonie = np.append(hypotonie, arr[i][1])
  return hypotonie
print(len(hypotonie(patients)))

#Wie viele Patienten haben Laktat > 2?
def high_laktat(arr):
  high_laktat = np.array([])
  for i in range(len(arr)):
    if arr[i][2] > 2:
      high_laktat = np.append(high_laktat, arr[i][2])
  return high_laktat
print(len(high_laktat(patients)))

#Wie viele erfüllen mindestens zwei Kriterien?
def criteria(arr):
  for i in range(len(arr)):
    if arr[i][0] > 100:
      arr[i][3] += 1
    if arr[i][1] < 90:
      arr[i][3] += 1
    if arr[i][2] > 2:
      arr[i][3] += 1
  
  many_criteria = np.array([])
  for i in range(len(arr)):
    if arr[i][3] > 1:
      many_criteria = np.append(many_criteria, arr[i][3])
  return len(many_criteria)

print(criteria(patients))


