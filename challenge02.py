import numpy as np

heart_rate = np.array([85, 92, 101, 115, 130])
rr = np.array([70, 82, 91, 105, 130])

def risk_mask(arr1, arr2):
  high_heart_rate = np.array([])
  high_rr = np.array([])
  for i in range(len(arr1)):
    if arr1[i] > 100:
      high_heart_rate = np.append(high_heart_rate, arr1[i])
  for i in range(len(arr2)):
    if arr2[i] < 90:
      high_rr = np.append(high_rr, arr2[i])
  return high_heart_rate, high_rr

print(risk_mask(heart_rate, rr))