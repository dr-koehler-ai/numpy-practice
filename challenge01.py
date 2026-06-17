import numpy as np

heart_rate = [85, 92, 101, 115, 130]
#mean heart rate
print(sum(heart_rate)/len(heart_rate))
# maximum heart rate
print(max(heart_rate))
# min heart rate
print(min(heart_rate))

array = np.array(heart_rate)
print(np.mean(array)) # mean heart rate
print(np.max(array)) # maximum heart rate
print(np.min(array)) # min heart rate
print(np.std(array)) # standard deviation