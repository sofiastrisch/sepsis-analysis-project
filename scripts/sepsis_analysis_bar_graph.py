import pandas as pd
import matplotlib.pyplot as plt

# Load aggregated dataset
data = pd.read_csv('sepsis_project_clean_aggregated.csv')

# Apply your sepsis pathway function


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

# Counts for actual septic patients
actual_septic_caught = sum(
    (data['SepsisLabel'] == 1) & (data['SepsisFlag'] == 1))
actual_septic_missed = sum(
    (data['SepsisLabel'] == 1) & (data['SepsisFlag'] == 0))

# Counts for patients flagged by pathway
flagged_correct = actual_septic_caught
flagged_false = sum((data['SepsisFlag'] == 1) & (data['SepsisLabel'] == 0))

# Prepare data for plotting
categories = ['Actual Septic Patients', 'Patients Flagged by Pathway']
caught_missed = [actual_septic_caught, flagged_correct]
missed_false = [actual_septic_missed, flagged_false]

# Plot
plt.figure(figsize=(8, 6))
plt.bar(categories, caught_missed,
        label='Correctly flagged / caught', color='darkred')
plt.bar(categories, missed_false, bottom=caught_missed,
        label='Missed / False alarms', color='orange')

plt.ylabel('Number of patients')
plt.title('Sepsis Pathway Performance')
plt.legend()
plt.show()
