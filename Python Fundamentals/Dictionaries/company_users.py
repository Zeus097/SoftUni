companies_information = {}

while True:
    command = input()

    if command == 'End':
        break

    information = command.split(" -> ")
    company_name = information[0]
    employee_id = information[1]

    if company_name not in companies_information:
        companies_information[company_name] = []
    if employee_id not in companies_information[company_name]:
        companies_information[company_name].append(employee_id)

for company_name, employees_id in companies_information.items():
    print(f"{company_name}")

    for employee_id in employees_id:
        print(f"-- {employee_id}")
