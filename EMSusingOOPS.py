#BLL
import json
import random

class Employee:
    emplist=[]
    ranidlist = []

    def __init__(self):
        self.id = ''
        self.name = ''
        self.address = ''
        self.mobile = ''
        self.type = ''

    def addEmployee(self):
        Employee.emplist.append(self)

    def getId(self):
        while(1):
            ran = str(random.randint(1000000, 999999))
            if ran not in Employee.ranidlist:
                Employee.ranidlist.append(ran)
                if self.type == 'manager':
                    return 'MGR' + ran
                elif self.type == 'trainer':
                    return 'TRR' + ran
                elif self.type == 'director':
                    return 'DIR' + ran

    @staticmethod
    def convtoDict(obj):
        return obj.__dict__

    @staticmethod
    def savetoJson():
        f = open("/Users/shubhamrawat/Desktop/emsjson.txt", "w")
        json.dump(Employee.emplist, f, default=Employee.convtoDict)
        f.close()

    @staticmethod
    def convtoObj(d):
        emp = Employee()
        emp.id = d['id']
        emp.name = d['name']
        emp.address = d['address']
        emp.mobile = d['mobile']
        emp.type = d['type']
        if (emp.type == 'manager'):
            emp.area = d['area']
        elif (emp.type == 'trainer'):
            emp.area = d['course']
        elif (emp.type == 'director'):
            emp.area = d['share']
        return emp

    @staticmethod
    def loadfromJson():
        f = open("/Users/shubhamrawat/Desktop/emsjson.txt", "r")
        Employee.emplist = json.load(f, object_hook=Employee.convtoObj)
        f.close()

class Manager(Employee):
    def __init__(self):
        self.area = ''
        super().__init__()

class Trainer(Employee):
    def __init__(self):
        self.course = ''
        super().__init__()

class Director(Employee):
    def __init__(self):
        self.share = ''
        super().__init__()

#PL
print()
print("- Hi There!! Welcome to the EMS -".center(100,'*'))

while(1):
    ch=input('''\nEnter
    1 to Add Customer
    2 to Search Customer
    3 to Delete Customer
    4 to Modify Customer
    5 to View All Customers
    6 to save to JSON
    7 to load from JSON
    x to Exit\n''')

    if (ch=='1'):
        while (1):
            ch1=input('''\nEnter
            1 to Add Manager
            2 to Add Trainer
            3 to Add Director\n''')

            if (ch1 == '1'): #Add Manager
                mgr = Manager()
                mgr.name = input("Enter Employee's Name: ")
                mgr.address = input("Enter Employee's Address: ")
                mgr.mobile = input("Enter Employee's Mobile No.: ")
                mgr.area = input("Enter Employee's Working Area: ")
                mgr.type = 'manager'
                mgr.id = mgr.getId()
                mgr.addEmployee()
                print("Employee Added Successfully!!!")
                break

            elif (ch1 == '2'):  # Add Trainer
                tr = Trainer()
                tr.name = input("Enter Employee's Name: ")
                tr.address = input("Enter Employee's Address: ")
                tr.mobile = input("Enter Employee's Mobile No.: ")
                tr.course = input("Enter Employee's Courses: ")
                tr.type = 'trainer'
                tr.id = tr.getId()
                tr.addEmployee()
                print("Employee Added Successfully!!!")
                break

            elif (ch1 == '3'):  # Add Director
                dir = Director()
                dir.name = input("Enter Employee's Name: ")
                dir.address = input("Enter Employee's Address: ")
                dir.mobile = input("Enter Employee's Mobile No.: ")
                dir.share = input("Enter Employee's Shares: ")
                dir.type = 'director'
                dir.id = dir.getId()
                dir.addEmployee()
                print("Employee Added Successfully!!!")
                break

            else:
                print("Invalid Input")
    elif (ch == '2'):
        pass
    elif (ch == '3'):
        pass
    elif (ch == '4'):
        pass
    elif (ch == '5'):
        for e in Employee.emplist:
            print(e.__dict__)
    elif (ch == '6'):
        Employee.savetoJson()
        print("Saved to json successfully.")
    elif (ch == '7'):
        Employee.loadfromJson()
        print("Load from json successfully.")
    elif (ch=='x' or ch=='X'):
        print("\nCheers!! Thanks for using this EMS")
        break
    else:
        print("Incorrect Input. Try Again!!")