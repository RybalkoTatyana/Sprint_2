class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours
    
    def get_email(self):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email
    
    @staticmethod
    def set_hourly_payment(new_hourly_payment):
        EmployeeSalary.hourly_payment = new_hourly_payment

    def salary(self):
        return self.get_hours() * EmployeeSalary.hourly_payment
    
# Пример:
EmployeeSalary.set_hourly_payment(350)
employee = EmployeeSalary("Иванов",rest_days=2)
print("Имя сотрудника:", employee.name, "количество выходных:", employee.rest_days, "зарплата:", employee.salary())
