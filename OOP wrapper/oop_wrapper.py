class Employee:# Class
    # Constrator
    def __init__(self , employee_id, name, age, salary):

        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def display(self):
        print(f"Employee created with name : {self.name} , age : {self.age}, ID : {self.__employee_id}, and salary: ${self.__salary}")

    # Setter
    def set_emp_id(self , set_id):
        if self.__employee_id == set_id:
            self.__employee_id = int(input("Enter Updated ID : "))
            print(f"{self.__employee_id} Updated Sucessfully.")
        else :
            print("This is Invaild ID.")

    # Setter
    def set_salary(self , set_salary):
        self.__salary = set_salary
        print(f"{self.__salary} Updated Sucessfully.")

    # Getter
    def get_emp_id(self):
        return print(f"Updated Employee ID : {self.__employee_id}")

    # Getter
    def get_salary(self):
        return print(f"Updated Salary : {self.__salary}")

    # destructor

    def __del__(self):
        print(f"{self.__employee_id} is deleted.")

    

print(" - - - Python OOP Project: Employee Management System - - - ")
while True:

    print("\nChoose an operation :")
    print("\n 1. Create a Person ")
    print(" 2. Create an Employee ")
    print(" 3. Create a Manager ")
    print(" 4. Show Details ")
    print(" 5. Exit ")

    choice = int(input("\nEnter your choice:  "))

    match choice:
        case 1 :
            employee_id = int(input("\nEnter Employee ID : "))
            name = input("Enter Employee Name : ")
            age = int(input("Enter Employee Age : "))
            salary = float(input("Enter Employee Salary : "))

            emp1 = Employee(employee_id, name, age, salary)
            while True:
                print("\n 1. Update  ")
                print(" 2. Display Choice ")
                print(" 3. Exit ")
                choice_emp = int(input("\n Enter Your choice : "))

                if choice_emp == 1:
                    print("\n 1. Employee ID ")
                    print(" 2. Salary")
                    choice1 = int(input("\n Enter Update choice :"))
                    if choice1 == 1:
                        emp_id = int(input("\n Enter Update Employee ID :"))
                        emp1.set_emp_id(emp_id)
                    elif choice1 == 2:
                        emp_salary = float(input("\n Enter Update Salary :"))
                        emp1.set_salary(emp_salary)
                    else:
                        print("\n Choice Only 1 and 2 Number. ")
                elif choice_emp == 2:
                    print("\n 1. Employee ID ")
                    print(" 2. Salary")
                    choice2 = int(input("\n Enter Display choice : "))
                    if choice2 == 1:
                        emp1.get_emp_id()
                    elif choice2 == 2:
                        emp1.get_salary()
                    else:
                        print("\n Choice Only 1 and 2 Number.")
                elif choice_emp == 3:
                    print("Main Menu ")
                    break
                else:
                    print("Enter Only 1 to 3 Number")
                    
        case 2 :
            print(" hiii ")
        case 3 :
            print(" hiii ")
        case 4 :
            print(" hiii ")
        case 5 :
            print(" Exit ")
            break
        case _:
            print("Enter Only 1 To 5 Number. ")

    
