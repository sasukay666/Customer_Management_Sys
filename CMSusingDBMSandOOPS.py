''''This program handles basic operations on a Customer Managaement System'''

#BLL
import pymysql

class Customer:

    Custlist=[]
    def __init__(self, name = '', address = '', mobile = ''):
        '''constuctor of Customer class to create and initialize variables of object'''
        self.id = -1
        self.name = name
        self.address = address
        self.mobile = mobile

    def addCustomer(self):
        '''addCustomer(self) takes the object as input from PL and
        runs INSERT INTO table query'''
        global con
        myCursor = con.cursor()
        strQuery = f"INSERT INTO cmscustomer (name, address, mobile) VALUES ('{self.name}', '{self.address}', '{self.mobile}')"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("Can't Insert Details Into Table")

    def searchCustomerByID(self):
        '''searchCustomerByID() searches for id in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE id = {self.id};"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            result = myCursor.fetchone()
            self.name = result[1]
            self.address = result[2]
            self.mobile = result[3]
        else:
            raise Exception("ID not Found")

    def searchCustomerByName(self):
        '''searchCustomerByID() searches for name in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE name = '{self.name}';"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected != 0:
            Customer.Custlist.clear()
            for row in myCursor.fetchall():
                cus = Customer()
                cus.id = row[0]
                cus.name = row[1]
                cus.address = row[2]
                cus.mobile = row[3]
                Customer.Custlist.append(cus)
        else:
            raise Exception("Name not Found")

    def searchCustomerByMobile(self):
        '''searchCustomerByID() searches for mobile in the cmscustomer table and returns the corresponding values'''
        myCursor = con.cursor()
        strQuery = f"SELECT * FROM cmscustomer WHERE mobile = '{self.mobile}';"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected != 0:
            result = myCursor.fetchone()
            self.name = result[1]
            self.address = result[2]
            self.id = result[0]
        else:
            raise Exception("Mobile not Found")

    def updateAll(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET name = '{self.name}', address = '{self.address}', mobile = '{self.mobile}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerName(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET name = '{self.name}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerAddress(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET address = '{self.address}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    def updateCustomerMobile(self):
        myCursor = con.cursor()
        strQuery = f"UPDATE cmscustomer SET mobile = '{self.mobile}' WHERE id = {self.id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("The ID you entered could not be found")

    @staticmethod
    def deleteCustomer(id):
        myCursor = con.cursor()
        strQuery = f"DELETE FROM cmscustomer WHERE id = {id}"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            con.commit()
        else:
            raise Exception("No matching record found for the id")

    @staticmethod
    def viewAll():
        '''This viewAll() function fetches all the entries from customer table.
        The reference object of each row is saved in a static list
        This static list Custlist can be accessed in PL using class name
        to access all the entries'''
        myCursor = con.cursor()
        strQuery = "SELECT * FROM cmscustomer;"
        rowAffected = myCursor.execute(strQuery)
        if rowAffected!=0:
            Customer.Custlist.clear()
            for row in myCursor.fetchall():
                cus = Customer()
                cus.id = row[0]
                cus.name = row[1]
                cus.address = row[2]
                cus.mobile = row[3]
                Customer.Custlist.append(cus)
        else:
            raise Exception("Table is Empty.")

    def login(host, user, password):
        '''This function takes host, user name and password from
        the user and creates a conncection using pymysql class'''
        global con
        con = pymysql.connect(host=host, user=user, password=password, database='cms_customer')

    global host, user, password             #global variables to allow access of database from all the implemented functions

##############################################################################################################################################

#PL
print()
print("- Hi There!! Welcome to the CMS -".center(100,'*'))

while(True):
        try:
            host = 'localhost'
            user = input("Enter UserName: ")
            password = input("Enter Password: ")
            Customer.login( host, user, password )
            print("- Login Successful!! -".center(100,'*'))
            break
        except Exception:
            print("Invalid Login Details!!. Try Again.")

while(1):
    ch=input('''\nEnter
    1 to Add Customer
    2 to Search Customer
    3 to Delete Customer
    4 to Modify Customer
    5 to View All Customers
    6 to Exit\n''')

    if(ch=="1"): #Add Customer
        try:
            ob = Customer()
            while(1):
                try:
                    ob.name = input("Enter Customer's Name: ").lower()
                    if ob.name.isalpha():
                        break
                    else:
                        raise NotImplementedError
                except NotImplementedError as err:
                    print("Numbers not allowed in Customer Name")
            ob.address = input("Enter Customer's Address: ")
            while(1):
                try:
                    ob.mobile=input("Enter Customer's Mobile No.: ")
                    if ob.mobile.isdigit()==False or len(ob.mobile)<10:
                        raise NotImplementedError
                    break
                except NotImplementedError:
                    print("Enter 10 digit number only")
            ob.addCustomer()
            print("Customer Added Successfully")
        except Exception as err:
            print("Error: ",err)

    elif(ch=="2"): #Search Customer
        cus=Customer()
        ch1=input('''Enter
        1 to search by ID
        2 to search by Name
        3 to search by Mobile No.\n''')
        if(ch1=='1'):
            try:
                cus.id=int(input("Enter Customer Id to Search: "))
                cus.searchCustomerByID()
                print("ID:", cus.id, "Name:", cus.name.title(), "Address:", cus.address.title(), "Mobile No.:", cus.mobile)
            except Exception as err:
                print("Error: ",err)
        elif(ch1=='2'):
            try:
                cus.name = input("Enter Customer Name to Search: ").lower()
                cus.searchCustomerByName()
                print("- ID -".center(5),"<-- Name -->".center(20),"<-- Address -->".center(20),"<-- Mobile No -->".center(12))
                for e in Customer.Custlist:
                    print(f"{e.id}".center(10), f"{e.name.title()}".center(20), f"{e.address.title()}".center(20),f"{e.mobile}".center(12))
                print(len(Customer.Custlist)," matching records found.")
            except Exception as err:
                print("Error: ",err)
        elif(ch1=='3'):
            try:
                cus.mobile = input("Enter Customer's Mobile No. to Search: ")
                cus.searchCustomerByMobile()
                print("ID:", cus.id, "Name:", cus.name.title(), "Address:", cus.address.title(), "Mobile No.:", cus.mobile)
            except Exception as err:
                print("Error: ",err)
        else:
            print("Incorrect Choice")


    elif(ch=="3"): #Delete Customer
        try:
            id=int(input("Enter ID of the customer to delete: "))
            Customer.deleteCustomer(id)
            print("Customer deleted successfully")
        except Exception as err:
            print("Error: ", err)


    elif(ch=="4"): #Update Customer
        cus=Customer()
        ch2=input('''Enter
        1 to edit all fields
        2 to edit Name
        3 to edit Address
        4 to edit Mobile No.\n''')
        if(ch2=='1'):
            try:
                cus.id = int(input("Enter ID to edit name: "))
                cus.name = input("Enter new name: ").lower()
                cus.address=(input("Enter new address: "))
                cus.mobile = (input("Enter new mobile no.: "))
                cus.updateAll()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)

        elif(ch2=='2'):
            try:
                cus.id=int(input("Enter ID to edit name: "))
                cus.name=input("Enter new name: ").lower()
                cus.updateCustomerName()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        elif(ch2=='3'):
            try:
                cus.id=int(input("Enter ID to edit address: "))
                cus.address=(input("Enter new address: "))
                cus.updateCustomerAddress()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        elif(ch2=='4'):
            try:
                cus.id = int(input("Enter ID to edit mobile no.: "))
                cus.mobile = (input("Enter new mobile no.: "))
                cus.updateCustomerMobile()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        else:
            print("Invalid Input!!")


    elif(ch=="5"): #View All Customers
        try:
            Customer.viewAll()
            print("- ID -".center(5),"<-- Name -->".center(20),"<-- Address -->".center(20),"<-- Mobile No -->".center(12))
            for e in Customer.Custlist:
                print(f"{e.id}.".rjust(5),"\t"+f"{e.name.title()}".ljust(20),f"{e.address.title()}".ljust(20),f"{e.mobile}".center(12))
        except Exception as err:
            print(err)


    elif(ch=="6"): #Exit
        global con
        con.close()
        print("\nCheers!! Thanks for using this CMS")
        break

    else:
        print("Incorrect Choice!!")