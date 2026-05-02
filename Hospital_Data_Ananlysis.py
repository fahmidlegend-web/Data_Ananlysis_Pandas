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
    "HeartRate": np.nan,
    "BloodPressure": np.nan,
    "Temperature": np.nan,
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

heartrateLow = [i for i in range(60,81)]
bloodpressureLow = [i for i in range(100,120)]

mask = (df["AdmissionType"] == "Elective") & (df["Diagnosis"] == "Normal")

df.loc[mask, "HeartRate"] = np.random.choice(heartrateLow, size=mask.sum(), replace=False)

df.loc[mask, "BloodPressure"] = np.random.choice(bloodpressureLow, size=mask.sum(), replace=False)


df.loc[mask, "Temperature"] = np.round(np.random.uniform(36, 38, size=mask.sum()), 1)

mask = (df["AdmissionType"] == "Elective") & (df["Diagnosis"] == "Normal") & (df["Age"] < 50) & (df["Temperature"] <= 38) & (df["BloodPressure"] <= 120) & (df["HeartRate"] <= 81)

df.loc[mask, "Outcome"] = "0.0"

mask = (df["AdmissionType"] == "Urgent") & (df["Diagnosis"] == "Diabetes")

df.loc[mask , "HeartRate"] = np.random.randint(90 , 100 , mask.sum())

df.loc[mask , "BloodPressure"] = np.random.randint(110 , 140 , mask.sum())

df.loc[mask,"Temperature"] = np.round(np.random.uniform(37 , 39 ,size = mask.sum()) , 1)

mask = mask = (df["AdmissionType"] == "Emergency") & (df["Diagnosis"] == "Diabetes")
df.loc[mask , "HeartRate"] = np.random.randint(90 , 100 , mask.sum())



df.loc[mask , "BloodPressure"] = np.random.randint(141 , 150 , mask.sum())
df.loc[mask,"Temperature"] = np.round(np.random.uniform(37 , 39 ,size = mask.sum()) , 1)

mask = (df["Age"] <= 55) & ((df["HeartRate"] >= 90) & (df["HeartRate"] <= 118)) & ( (df["BloodPressure"] >= 110) &(df["BloodPressure"] ) <= 150) 

df.loc[mask,"Outcome"] = "0.4"

mask = ((df["Age"] <= 70) & (df["Age"] >= 55)) & ((df["HeartRate"] >= 90) & (df["HeartRate"] <= 118)) & ( (df["BloodPressure"] >= 110) & (df["BloodPressure"] <= 150) )

df.loc[mask,"Outcome"] = "0.7"


mask =  (df["AdmissionType"] == "Emergency") 



df.loc[mask, "Temperature"] = np.round(np.random.uniform(37,39 , size = mask.sum()) , 1)
df.loc[mask, "BloodPressure"] = np.random.randint(155 , 170 , mask.sum())
df.loc[mask, "HeartRate"] = np.random.randint(112 , 130, mask.sum())



mask = (df["Age"] >= 65) & ((df["HeartRate"] >= 112) & (df["HeartRate"] <= 130)) & ( (df["BloodPressure"] >= 155) &(df["BloodPressure"] ) <= 170) 

df.loc[mask,"Outcome"] = "1.0"

df =df.drop(columns = ["Medication" ,"GlucoseLevel" ,"Gender"])

mask =  ((df["AdmissionType"] == "Emergency") | (df["AdmissionType"] == "Urgent"))&(df["Diagnosis"] == "Sepsis")



df.loc[mask, "Temperature"] = np.round(np.random.uniform(37,39 , size = mask.sum()) , 1)
df.loc[mask, "BloodPressure"] = np.random.randint(155 , 190 , mask.sum())
df.loc[mask, "HeartRate"] = np.random.randint(130, 150, mask.sum())
df.loc[mask,"Outcome"] = "1.0"

mask = (df["Age"] >= 80) & (df["AdmissionType"] == "Urgent")

df.loc[mask,"Outcome"] = np.random.choice(["0.7","1.0"], mask.sum())

mask = ((df["Age"] >= 55) & (df["Age"] <= 70)) & (df["AdmissionType"] == "Urgent")

df.loc[mask,"Outcome"] = "0.7"

mask = (df["Age"] <= 70) & (df["AdmissionType"] == "Urgent")

df.loc[mask,"Outcome"] = "0.7"
#mask =(df["Age"] >= 55) & ()
mask = (df["Age"] <= 70) & (df["Diagnosis"] == "Hypertension") 

df.loc[mask,"Outcome"] = "0.7"

mask = (df["Age"] <= 70) & (df["Diagnosis"] == "Sepsis")

df.loc[mask,"Outcome"] = "1.0"


mask = (df["Diagnosis"] == "Sepsis")

df.loc[mask , "HeartRate"] = np.random.randint(120, 150, mask.sum())
df.loc[mask , "BloodPressure"] = np.random.randint(130, 190, mask.sum())
df.loc[mask , "Temperature"] = np.round(np.random.uniform(37,39 , size = mask.sum()) , 1)



mask = ((df["Age"] > 55) & (df["Age"] <= 70))& ((df["AdmissionType"] == "Elective") | (df["AdmissionType"] == "Urgent") ) & ((df["Diagnosis"] == "Hypertension") | (df["Diagnosis"] == "Diabetes"))

df.loc[mask , "Outcome"] = "0.7"

mask = (df["Age"] > 70) & ((df["AdmissionType"] == "Elective") | (df["AdmissionType"] == "Urgent") ) & ((df["Diagnosis"] == "Hypertension") | (df["Diagnosis"] == "Diabetes"))

df.loc[mask , "Outcome"] = "1.0"

mask = (df["Age"] > 70) & ((df["AdmissionType"] == "Emergency")  ) & ((df["Diagnosis"] == "Hypertension") | (df["Diagnosis"] == "Diabetes"))

df.loc[mask , "Outcome"] = "1.0"

mask = (df["Age"] > 70) & ((df["AdmissionType"] == "Emergency") |
(df["AdmissionType"] == "Elective"))& ((df["Diagnosis"] == "Normal") )

df.loc[mask , "Outcome"] = np.random.choice(["0.7" , "1.0" ], mask.sum())

df["Outcome"].iloc[93] = "0.0"
#print(df["Outcome"].iloc[93])
mask = (df["Age"] < 55) & (df["AdmissionType"] == "Emergency") & ((df["Diagnosis"] == "Hypertension") | (df["Diagnosis"] == "Normal"))
df.loc[mask , "Outcome"] = "0.4"
df["Outcome"].iloc[18] = "0.4"
df["Outcome"].iloc[13] = "1.0"

mask = (df["Age"] <= 55) & ((df["AdmissionType"] == "Elective")  ) & ((df["Diagnosis"] == "Hypertension") | (df["Diagnosis"] == "Diabetes"))

df.loc[mask , "Outcome"] = "0.4"

print(df.loc[df["Outcome"].isna()])

df["Outcome"].iloc[17] = "0.7"
df["Outcome"].iloc[28] = "0.4"
df["Outcome"].iloc[43] =  "1.0"
df["Outcome"].iloc[45] =  "0.7"
df["Outcome"].iloc[59] = "0.4"
df["Outcome"].iloc[66] = "1.0"
df["Outcome"].iloc[68] = "0.7"

mask = (df["AdmissionType"] == "Urgent") & (df["Diagnosis"] == "Normal")

df.loc[mask , "HeartRate"] = np.random.randint(70 , 90 , mask.sum())

df.loc[mask , "BloodPressure"] = np.random.randint(110 , 130 , mask.sum())

df.loc[mask,"Temperature"] = np.round(np.random.uniform(36 , 38 ,size = mask.sum()) , 1)


mask = (df["AdmissionType"] == "Urgent") & (df["Diagnosis"] == "Hypertension")

df.loc[mask , "HeartRate"] = np.random.randint(112 , 118 , mask.sum())

df.loc[mask , "BloodPressure"] = np.random.randint(130 , 170 , mask.sum())

df.loc[mask,"Temperature"] = np.round(np.random.uniform(38 , 39 ,size = mask.sum()) , 1)


mask = (df["AdmissionType"] == "Elective") & (df["Diagnosis"] == "Diabetes")

df.loc[mask , "HeartRate"] = np.random.randint(80 , 90 , mask.sum())

df.loc[mask , "BloodPressure"] = np.random.randint(110 , 130 , mask.sum())

df.loc[mask,"Temperature"] = np.round(np.random.uniform(37 , 38 ,size = mask.sum()) , 1)

mask = (df["AdmissionType"] == "Elective") & (df["Diagnosis"] == "Hypertension")

df.loc[mask , "HeartRate"] = np.random.randint(100 , 110 , mask.sum())

df.loc[mask , "BloodPressure"] = np.random.randint(130 , 170 , mask.sum())

df.loc[mask,"Temperature"] = np.round(np.random.uniform(37, 39 ,size = mask.sum()) , 1)

df.to_csv("/storage/emulated/0/Documents/CSV Viewer/Hospital_test.csv",index = False)
