class Employee:
    ANNUAL_SALARY = 12

    def __init__(self, id_: int, first_name: str, last_name: str, salary: int):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        return self.salary * Employee.ANNUAL_SALARY

    def raise_salary(self, amount: str) -> None:
        self.salary += amount
        return self.salary


# Test code
# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())
