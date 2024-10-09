import pandas as pd
import numpy as np
import random

Number_of_patients = 1000
PatientID = np.random.randint(1, 101, size = Number_of_patients)
print(PatientID)

Age = np.random.randint(50, 81, size = Number_of_patients)
print(Age)

Gender = np.random.choice(["Male", "Female"], size = Number_of_patients)
print(Gender)

tuma_size = np.round(np.random.uniform(0.2, 15.0, size = Number_of_patients), 2)
print(tuma_size)

Cancer_stage = np.random.choice(["I", "II", "III", "IV"], size = Number_of_patients)
print(Cancer_stage)

survived = np.random.choice(["No", "Yes"], size = Number_of_patients)
print(survived)

key = pd.DataFrame({
    'PatientID': PatientID, 'Age': Age, 'Gender': Gender, 'Tuma_Size': tuma_size, 'Cancer_Stage': Cancer_stage, 'Survived': survived
})

print(key.info())