import pandas as pd

# Load dataset
data = pd.read_csv('prediction_of_sepsis.csv')

# Keep only relevant columns for your sepsis detection tool
vitals_labs = [
    'HR', 'SBP', 'DBP', 'MAP', 'Resp', 'Temp', 'O2Sat',
    'WBC', 'Lactate', 'Creatinine', 'Bilirubin_total', 'Platelets',
    'SepsisLabel', 'Patient_ID'
]

data = data[vitals_labs]

# Drop duplicates
data = data.drop_duplicates()

# Drop rows with too many missing values (≥70% non-NaN)
data = data.dropna(thresh=int(len(data.columns) * 0.7))

# Fill remaining missing numeric values with column means
data = data.fillna(data.mean(numeric_only=True))

# Clinically realistic aggregation per patient
agg_dict = {
    'HR': 'mean',                  # average heart rate
    'SBP': 'min',                  # lowest systolic BP
    'DBP': 'min',                  # lowest diastolic BP
    'MAP': 'min',                  # lowest mean arterial pressure
    'Resp': 'mean',                # average respiratory rate
    'Temp': 'max',                 # highest temperature
    'O2Sat': 'min',                # lowest oxygen saturation
    'WBC': 'max',                  # highest WBC
    'Lactate': 'max',              # highest lactate
    'Creatinine': 'max',           # highest creatinine
    'Bilirubin_total': 'max',      # highest bilirubin
    'Platelets': 'min',            # lowest platelets
    'SepsisLabel': 'max'           # patient is flagged if any row had sepsis
}

# Group by patient
patient_data = data.groupby('Patient_ID').agg(agg_dict).reset_index()

# Round values for readability
patient_data = patient_data.round(2)

# Save aggregated dataset
patient_data.to_csv('sepsis_project_clean_aggregated.csv', index=False)

print("✅ Aggregation complete. Saved as sepsis_project_clean_aggregated.csv.")
print(f"Final shape: {patient_data.shape}")
print("Columns:", list(patient_data.columns))
