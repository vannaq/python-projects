#This is a mini project about tracking patients' medication logs and vitals. 
import pandas as pd

df = pd.read_csv('./misc_projects/patient_tracker/patient_vitals_log.csv')          #Loads CSV file using pd.read_csv()
records = df.to_dict(orient="records")                                              #Converts DataFrame to a list of dictionaries

patient_at_risk = 0                                                                 #Define variable called patient_at_risk to begin counter
alert_patients = []

for patients in records:
    if (patients['systolic_bp'] > 140) or (patients['diastolic_bp'] > 90) or (patients['temperature'] > 100.4):
        patient_at_risk = patient_at_risk + 1
        alert_patients.append(patients)
        print(f'{patients["name"]}: High BP or FEVER. On antiobiotics: {patients["on_antibiotics"]}')
    else: 
        print(f'{patients["name"]}: Normal. On antibiotics: {patients["on_antibiotics"]}')

print(f'Total patients with high BP or fever: {patient_at_risk}')                   #Print how many patients have fevers or high BP. Note: This needs to be OUTSIDe of the for loop, otherwise it will show the count after every increment which is messy and confusing.

alert_df = pd.DataFrame(alert_patients)                                                 #Converts list of alert_patients back into a DataFrame
# sorted_temp_df = alert_df.sort_values(by="temperature", ascending=False)              #Sorts values by temperature, e.g. by="column to sort by" and ascending=False states highest values first.
# sorted_bp_df = alert_df.sort_values(by="systolic_bp", ascending=False)                #Sorts values by systolic bp, from highest to lowest
# print(sorted_temp_df)                                                                 #Print values to check the sorting
# print(sorted_bp_df)
sorted_combined_df = alert_df.sort_values(by=['systolic_bp', 'diastolic_bp'], ascending=[False, False])     #Sort by both, systolic first then if tied, diastolic (also highest first).
print(sorted_combined_df)

sorted_combined_df.to_csv("./misc_projects/patient_tracker/sorted_patient_alerts.csv", index=False)      #Exports DataFrame into a csv
    