company_details = input()

companies = {}

while company_details != "End":

    company_name, employees_id = company_details.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
    if employees_id not in companies[company_name]:
        companies[company_name].append(employees_id)

    company_details = input()

for company, employee_id in companies.items():
    print(f"{company}")
    for i in employee_id:
        print(f"-- {i}")
