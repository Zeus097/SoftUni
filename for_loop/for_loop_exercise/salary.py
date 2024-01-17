number_of_opened_tabs = int(input())
salary = int(input())

for web_browsing in range(number_of_opened_tabs):
    web_site_name = input()
    if web_site_name == "Facebook":
        salary -= 150
    elif web_site_name == "Instagram":
        salary -= 100
    elif web_site_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")