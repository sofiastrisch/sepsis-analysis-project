import pandas as pd

data = pd.read_csv('sepsis_project_clean_aggregated.csv')



def sepsis_flag(row):
    score = 0
    if row['HR'] > 100:
        score += 1
    if row['SBP'] < 90 or row['MAP'] < 65:
        score += 2
    if row['Resp'] < 10 or row['Resp'] > 22:
        score += 1
    if row['Temp'] > 38 or row['Temp'] < 36:
        score += 1
    if row['O2Sat'] < 92:
        score += 1
    if row['WBC'] < 4 or row['WBC'] > 12:
        score += 1
    if row['Lactate'] > 2:
        score += 2
    if row['Creatinine'] > 1.5:
        score += 1
    if row['Bilirubin_total'] > 2:
        score += 1
    if row['Platelets'] < 100:
        score += 1
    return 1 if score >= 6 else 0



data['SepsisFlag'] = data.apply(sepsis_flag, axis=1)


total_patients = len(data)

total_septic = sum(data['SepsisLabel'] == 1)

patients_flagged = sum(data['SepsisFlag'] == 1)
correctly_flagged = sum((data['SepsisFlag'] == 1) & (
    data['SepsisLabel'] == 1))  # flagged AND actually septic

# Percentages
percent_of_septic_caught = correctly_flagged / total_septic * 100
percent_of_flagged_were_septic = correctly_flagged / patients_flagged * 100


print("=== Sepsis Pathway Performance ===")
print(f"Total patients: {total_patients}")
print(f"Number of patients who actually had sepsis: {total_septic}")
print(f"Number of patients flagged by the pathway: {patients_flagged}")
print(
    f"Number of flagged patients who actually had sepsis: {correctly_flagged}")
print(
    f"Percentage of actual septic patients your pathway caught: {percent_of_septic_caught:.1f}%")
print(
    f"Percentage of flagged patients who really were septic: {percent_of_flagged_were_septic:.1f}%")
