#Business Logic Layer
idlist=[]
agelist=[]
namelist=[]
ide = 140000

def addCustomer(age,name):
    global ide
    idlist.append(ide)
    agelist.append(age)
    namelist.append(name.lower())
    ide+=1

def searchCustomerbyID(id):
    index=idlist.index(id)
    return index

def searchCustomerbyName(name):
    ls=[]
    count=namelist.count(name)
    if(count==0):
        print("Name not found")
    else:
        for i in range (len(namelist)):
            if(namelist[i]==name):
                ls.append(i)
    return ls


def deleteCustomer(id):
    index=idlist.index(id)
    idlist.pop(index)
    agelist.pop(index)
    name=namelist.pop(index)
    return name

def updateName(id,name):
    index=idlist.index(id)
    namelist[index] = name

def updateAge(id,age):
    index = idlist.index(id)
    agelist[index] = age

#Presentation Layer

print("Welcome")

while(1):
    ch=input('''\nEnter Choice 1 for Add Cust, 2 for Search Cust
    3 for Delete Cust, 4 for Modify Cust, 5 to View All, 6 to Exit:\n''')


    if(ch=="1"): #Add Customer

        age='p'
        while(age.isalnum()):
            age=input("Enter Cust Age:")
            if(age.isnumeric() and int(age)>0 and int(age)<120):
                break
            else:
                print("Incorrect input. Enter correct age.")
        age=int(age)

        name=input("Enter Cust Name:")
        addCustomer(age,name)
        print("Customer Added Successfully")


    elif(ch=="2"): #Search Customer
        ch1=input("1 to search by ID, 2 to search by name:")
        if(ch1=='1'):
            id=int(input("Enter Cust Id to Search:"))
            i=searchCustomerbyID(id)
            print("Cust Id:", idlist[i], "Cust Age:", agelist[i], "Cust Name:", namelist[i].title())
        elif(ch1=='2'):
            name=input("Enter Cust Name to Search:")
            ls=searchCustomerbyName(name)
            for i in ls:
                print("Cust Id:",idlist[i],"Cust Age:",agelist[i],"Cust Name:",namelist[i].title())
        else:
            print("Incorrect Choice")


    elif(ch=="3"): #Delete Customer
        id=int(input("Enter Cust Id to Delete:"))
        name=deleteCustomer(id)
        print(f"Cust with Id: {id} and Name: {name} delete successfully")


    elif(ch=="4"): #Update Customer

        ch2=input("Enter 1 to edit Name, 2 to edit age")
        if(ch2=='1'):
            id=int(input("Enter ID to edit name"))
            n_name=input("Enter new name")
            updateName(id,n_name)
        elif(ch2=='2'):
            id=int(input("Enter ID to edit age"))
            n_age=int(input("Enter new age"))
            updateAge(id, n_age)

        print("Customer details updated successfully")


    elif(ch == "5"): #View All Customers
        print("Cust Id:".center(20),"Cust Age:".center(20),"Cust Name:".center(20))
        for i in range (len(idlist)):
            print(f"{idlist[i]}".center(20),f"{agelist[i]}".center(18),f"{namelist[i].title()}".center(24))


    elif(ch=="6"): #Exit
        print("\nCheers!!")
        break

    else:
        print("Incorrect Choice")