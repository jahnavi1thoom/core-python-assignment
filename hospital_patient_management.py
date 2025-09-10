
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
def find_patients_by_disease(patient_list, disease):
    return [patient["Name"] for patient in patient_list if patient["Disease"] == disease]
matching_patients = find_patients_by_disease(patients, search_disease)
print(f'Patients with {search_disease}: {matching_patients}')
