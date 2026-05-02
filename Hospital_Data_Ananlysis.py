import pandas as pd
import numpy as np
from datetime import datetime
import random as rd

np.random.seed(42)
n = 100




datetime_Obj = [ ]


for i in range(7,9):
    for j in range(7,12):
        if i < 10 and j < 10:
            
            datetime_Obj.append(f"0{i}:0{j}:00")
        elif i < 10 and j >=10:
            datetime_Obj.append(f"0{i}:{j}:00")
        else:
            datetime_Obj.append(f"{i}:{j}:00")
            
dateTest = pd.to_datetime(datetime_Obj , format = "%H:%M:%S")


datetime_Obj2 = [ ]
for i in range(12,14):
    for j in range(7,12):
        if j < 10:
            datetime_Obj2.append(f"{i}:0{j}:00")
        else:
            datetime_Obj2.append(f"{i}:{j}:00")
        
dateTest2 = pd.to_datetime(datetime_Obj2, format = "%H:%M:%S")
test_list = [dt.time().strftime("%H:%M") for dt in dateTest]
test_list2 = [dt.time().strftime("%H:%M") for dt in dateTest2]

df = pd.DataFrame({
    "PatientID": range(1, n+1),
    "Age": np.random.randint(18, 90, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "AdmissionType": np.random.choice(["Emergency", "Urgent", "Elective"], n),
    "HeartRate": np.random.randint(60, 150, n),
    "BloodPressure": np.random.randint(80, 180, n),
    "Temperature": np.round(np.random.uniform(36, 41, n), 1),
    "GlucoseLevel": np.random.randint(70, 200, n),
    "Arrival_Time" : np.random.choice(test_list , n),
    "Departure_Time" : np.random.choice(test_list2 , n) ,
    "Diagnosis": np.random.choice(["Diabetes", "Sepsis", "Hypertension", "Normal"], n),
    "Medication": np.random.choice(["DrugA", "DrugB", "DrugC"], n),
    "Outcome": np.nan
    # 1 = death, 0 = survive
})
df["Arrival_Time"] = df["Arrival_Time"].astype(str) + "  am"
df["Departure_Time"] = df["Departure_Time"].astype(str) + "  pm"

df["Diagnosis"].loc[(df["Age"]  <= 40) & (df["AdmissionType"] =="Elective") & (df["BloodPressure"] <= 100) & (df["Temperature"] <= 38) ] = "Normal"



df["Outcome"].loc[(df["Age"]  <= 40) & (df["AdmissionType"] =="Elective") & (df["BloodPressure"] <= 130) & (df["Diagnosis"] == "Normal") & (df["Temperature"] <= 38) | (df["HeartRate"] <= 110)] = "0"



df.to_csv("/storage/emulated/0/Documents/CSV Viewer/Hospital_test.csv",index = False)