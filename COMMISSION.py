class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        pass  


class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission

emp1 = SalaryEmployee(101, "Angel", 6000)
emp2 = HourlyEmployee(102, "Kyle", 40, 50)  
emp3 = CommissionEmployee(103, "Ellah", 5000, 1500)

print("Payroll Summary")
print(f"{emp1.name}: {emp1.calculate_payroll()}")
print(f"{emp2.name}: {emp2.calculate_payroll()}")
print(f"{emp3.name}: {emp3.calculate_payroll()}")
