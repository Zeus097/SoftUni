researched_time_needed= int(input())
treated_patients = 0
untreated_patients = 0
doctor_numbers = 7

for days in range(1, researched_time_needed +1):
    patients_number = int(input())
    if days % 3 == 0 and untreated_patients > treated_patients :
        doctor_numbers += 1
    if doctor_numbers >= patients_number:
        treated_patients += patients_number
    else:
        untreated_patients += patients_number - doctor_numbers
        treated_patients += doctor_numbers

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")