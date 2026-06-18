import numpy as np

hr = np.array([80, 110, 130, 90, 150])
rr = np.array([120, 85, 70, 95, 60])
lactate = np.array([1.0, 2.5, 3.0, 0.8, 4.2])

patients = np.concatenate((hr.reshape(5,1), rr.reshape(5,1), lactate.reshape(5,1)), axis=1)
scores = np.zeros(5).reshape(5,1)
patients = np.hstack((patients, scores))

tachy = patients[:,0] > 100
hypo = patients[:,1] < 90
lac = patients[:,2] > 2

score = tachy.astype(int) + hypo.astype(int) + lac.astype(int)

patients[:,3] = score

def risk_class(score):
    if score <= 1:
        return "low"
    elif score == 2:
        return "medium"
    else:
        return "high"

risk_classes = [risc_class(s) for s in patients[:,3]]
patients = np.hstack((patients, np.array(risk_classes).reshape(-1,1)))

print(patients)