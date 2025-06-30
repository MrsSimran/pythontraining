class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Simran", 50000)
e1.info()
