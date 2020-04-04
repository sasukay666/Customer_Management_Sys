#BLL
import json
import pickle

class Customer:
    ran=100
    Custlist=[]
    def __init__(self,name='',address='',mobile_no=''):
        self.id=Customer.ran
        self.name=name
        self.address=address
        self.mobile_no=mobile_no

    def addCustomer(self):
        Customer.Custlist.append(self)
        Customer.ran+=1

    def searchCustomerByID(self):
        for e in Customer.Custlist:
            if(e.id==self.id):
                self.name=e.name
                self.address=e.address
                self.mobile_no=e.mobile_no
    def searchCustomerByName(self):
        for e in Customer.Custlist:
            if (e.name == self.name):
                self.id = e.id
                self.address = e.address
                self.mobile_no = e.mobile_no
    def searchCustomerByMobile(self):
        for e in Customer.Custlist:
            if (e.mobile_no == self.mobile_no):
                self.name = e.name
                self.address = e.address
                self.id = e.id

    @staticmethod
    def deleteCutstomer(id):
        for e in Customer.Custlist:
            if(e.id==id):
                Customer.Custlist.remove(e)

    def updateCustomerName(self):
        for e in Customer.Custlist:
            if(e.id==self.id):
                e.name=self.name;

    def updateCustomerAddress(self):
        for e in Customer.Custlist:
            if(e.id==self.id):
                e.address=self.address;

    def updateCustomerMobileNo(self):
        for e in Customer.Custlist:
            if(e.id==self.id):
                e.mobile_no=self.mobile_no;

    @staticmethod
    def viewAll():
        return Customer.Custlist

    @staticmethod
    def convtoDict(obj):
        return obj.__dict__

    @staticmethod
    def savetoJson():
        f = open("/Users/shubhamrawat/Desktop/cmsjson.txt","w")
        json.dump(Customer.Custlist, f, default=Customer.convtoDict)
        f.close()

    @staticmethod
    def convtoObj(d):
        cus = Customer()
        cus.id = d['id']
        cus.name = d['name']
        cus.address = d['address']
        cus.mobile_no = d['mobile_no']
        return cus

    @staticmethod
    def loadfromJson():
        f = open("/Users/shubhamrawat/Desktop/cmsjson.txt", "r")
        Customer.Custlist = json.load( f, object_hook=Customer.convtoObj)
        f.close()

    @staticmethod
    def savetoPickle():
        f = open("/Users/shubhamrawat/Desktop/cmspickle.txt","wb")
        pickle.dump(Customer.Custlist, f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("/Users/shubhamrawat/Desktop/cmspickle.txt","rb")
        Customer.Custlist = pickle.load(f)
        f.close()

#PL
print()
print(" Hi There!! Welcome to the CMS ".center(100,'*'))

while(1):
    ch=input('''Enter
    1 to Add Customer
    2 to Search Customer
    3 to Delete Customer
    4 to Modify Customer
    5 to View All Customers
    6 to save to JSON
    7 to load from JSON
    8 to save to Pickle
    9 to load from Pickle
    x to Exit:\n''')

    if(ch=="1"): #Add Customer
        try:
            ob=Customer()
            ob.name=input("Enter Customer's Name: ").lower()
            ob.address=input("Enter Customer's Address: ")
            while(1):
                try:
                    ob.mobile_no=input("Enter Customer's Mobile No.: ")
                    if ob.mobile_no.isdigit()==False or len(ob.mobile_no)<10:
                        raise NotImplementedError
                    break
                except NotImplementedError as err:
                    print("Enter 10 digits number only")
            ob.addCustomer()
            print("Customer Added Successfully")
        except Exception as err:
            print("Error: ",err)

    elif(ch=="2"): #Search Customer
        cus=Customer()
        ch1=input("1 to search by ID, 2 to search by Name, 3 to search by Mobile No.: ")
        if(ch1=='1'):
            try:
                cus.id=int(input("Enter Customer Id to Search: "))
                cus.searchCustomerByID()
                print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(), "Cust Mobile No.:", cus.mobile_no)
            except Exception as err:
                print("Error: ",err)
        elif(ch1=='2'):
            cus.name = input("Enter Customer Name to Search: ").lower()
            cus.searchCustomerByName()
            print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(), "Cust Mobile No.:", cus.mobile_no)
        elif(ch1=='3'):
            cus.mobile_no = input("Enter Customer's Mobile No. to Search: ")
            cus.searchCustomerByMobile()
            print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(), "Cust Mobile No.:", cus.mobile_no)
        else:
            print("Incorrect Choice")


    elif(ch=="3"): #Delete Customer
        try:
            id=int (input("Enter ID of the customer to delete: "))
            Customer.deleteCutstomer(id)
            print(f"Customer deleted successfully")
        except Exception as err:
            print("Error: ", err)


    elif(ch=="4"): #Update Customer
        cus=Customer()
        ch2=input("Enter 1 to edit Name, 2 to edit Address, 3 to edit Mobile No.: ")
        if(ch2=='1'):
            try:
                cus.id=int(input("Enter ID to edit name: "))
                cus.searchCustomerByID()
                print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(),
                      "Cust Mobile No.:", cus.mobile_no)
                cus.name=input("Enter new name: ").lower()
                cus.updateCustomerName()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        elif(ch2=='2'):
            try:
                cus.id=int(input("Enter ID to edit address: "))
                cus.searchCustomerByID()
                print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(),
                      "Cust Mobile No.:", cus.mobile_no)
                cus.address=(input("Enter new address: "))
                cus.updateCustomerAddress()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        elif(ch2=='3'):
            try:
                cus.id = int(input("Enter ID to edit mobile no.: "))
                cus.searchCustomerByID()
                print("Cust Id:", cus.id, "Cust Name:", cus.name.title(), "Cust Address:", cus.address.title(),
                      "Cust Mobile No.:", cus.mobile_no)
                cus.mobile_no = (input("Enter new mobile no.: "))
                cus.updateCustomerMobileNo()
                print("Customer details updated successfully")
            except Exception as err:
                print("Error: ", err)
        else:
            print("Invalid Input!!")


    elif(ch=="5"): #View All Customers
        print("Cust Id:".center(20),"Cust Name:".center(20),"Cust Address:".center(20),"Cust Mobile No.")
        Custlist=Customer.viewAll()
        for e in Custlist:
            print(f"{e.id}".center(20),f"{e.name.title()}".center(20),f"{e.address.title()}".center(20),f"{e.mobile_no}".center(12))

    elif(ch=="6"): #Save to JSON
        Customer.savetoJson()
        print("Saved to json successfully.")

    elif(ch=="7"): #Load from JSON
        Customer.loadfromJson()
        print("Load from json successful.")

    elif(ch=="8"): #Load to pickle
        Customer.savetoPickle()
        print("Saved to pickle successfully.")
        pass

    elif(ch=="9"): #Load from Pickle
        Customer.loadfromPickle()
        print("Load from pickle successfully.")
        pass

    elif(ch=="x" or ch=="X"): #Exit
        print("\nCheers!! Thanks for using this CMS")
        break

    else:
        print("Incorrect Choice")