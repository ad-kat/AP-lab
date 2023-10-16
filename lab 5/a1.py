class Employee:
    
    last_employee_id = 2911

    def __init__(self, name, salary, department):
        
        Employee.last_employee_id += 1
        self.id = Employee.last_employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def __del__(self):
        print(f"Employee {self.id} ({self.name}) has been removed.")

    def display(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")

    @classmethod
    def total_salary(cls, employees):
        total = sum(emp.salary for emp in employees)
        return total

# Create a list to store employee instances
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Display Employee Details")
    print("3. Total Salary of All Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee's name: ")
        salary = float(input("Enter employee's salary: "))
        department = input("Enter employee's department: ")
        emp = Employee(name, salary, department)
        employees.append(emp)
        print(f"Employee {emp.id} ({emp.name}) added.")

    elif choice == '2':
        emp_id = int(input("Enter the employee ID to display details: "))
        for emp in employees:
            if emp.id == emp_id:
                emp.display()
                break
        else:
            print(f"Employee with ID {emp_id} not found.")

    elif choice == '3':
        total = Employee.total_salary(employees)
        print(f"Total salary of all employees: ${total}")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
