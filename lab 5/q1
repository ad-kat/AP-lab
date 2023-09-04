class Employee:
    """Base class for employees."""

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def get_details(self):
        """Returns the employee details."""
        return (self.id, self.name, self.salary, self.department)



def read_employee_details():
    

    n = int(input("Enter the number of employees: "))
    employees = []
    for i in range(n):
        id = input("Enter the employee ID: ")
        name = input("Enter the employee name: ")
        salary = input("Enter the employee salary: ")
        department = input("Enter the employee department: ")
        employees.append(Employee(id, name, salary, department))

    return employees


def main():
    
    employees = read_employee_details()

    id = input("Enter id to search: ")
    employee = None
    for emp in employees:
        if emp.id == id:
            employee = emp
            break

    if employee is not None:
        print("Employee details:")
        print(employee.get_details())
    else:
        print("Employee record not found.")


main()
