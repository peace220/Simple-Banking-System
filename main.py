# SIM JING ZHI
# TP066307
from datetime import datetime


def Superlogin():
    SuperUserId = input("Enter Super User Id: ")
    SuperUserPassword = input("Enter Password: ")
    if SuperUserId == "configuration123" and SuperUserPassword == "SuperUser1234":  # validate correct user id and password
        return adminregistration()
    else:
        print("Invalid Id or Password")
        return Superlogin()


def adminregistration():  # allow user to register a new data
    while True:
        Adminlist = []
        AdminUserId = input("For admin registration: \nEnter admin user id: ")
        AdminPassword = input("Enter admin password: ")

        Fadmin = open("admininfo.txt", "r")
        adminRawData = Fadmin.readlines()
        Fadmin.close()
        adminList = []
        for record in adminRawData:  # turn file text data into a list
            adminNewData = record.strip().split("\t")
            adminList.append(adminNewData)

        for searchdata in adminList:  # use the search the file text data line by line using a substitude list
            AdminUser = searchdata[0]
            if AdminUser == AdminUserId:  # search if user entered data is already existed inside the text file
                print("there is a existing ID that you have entered: ", AdminUserId)
                return adminregistration()
            else:
                continue

        Adminlist.append(AdminUserId)
        Adminlist.append(AdminPassword)
        Alist = "\t".join(Adminlist)
        Wadmin = open("admininfo.txt", "a")
        Wadmin.write(Alist)
        Wadmin.write("\n")
        Wadmin.close()
        while True:
            cont = input("Enter 1 to continue\nEnter 2 to quit: ")
            if cont == "1":
                break
            elif cont == "2":
                return
            else:
                print("Invalid input")
                continue


# -------------------------------------------------------------------------------------------------------------------------------------------------
def Adminlogin():
    while True:
        AdminUserId = input("Enter Admin User Id: ")
        AdminPassword = input("Enter Admin Password: ")
        Radmin = open("admininfo.txt", "r")
        adminRawData = Radmin.readlines()
        Radmin.close()
        adminList = []

        for record in adminRawData:  # turn file text data into a list
            adminNewData = record.strip().split("\t")
            adminList.append(adminNewData)

        for searchdata in adminList:  # use the search the file text data line by line using a substitude list
            FileAdminUser = searchdata[0]
            FileAdminPassword = searchdata[1]
            if FileAdminUser == AdminUserId and FileAdminPassword == AdminPassword:  # validate if user entered data and file text data are the same
                print("Welcome ", AdminUserId)
                return adminchoise()
            else:
                continue
        print("invalid id or password please retry")
        continue


def adminchoise():
    AdminChoise = input("enter 1 to register customer account: \nEnter 2 to edit customer account: \nEnter 3 to print Customer Account Report: ")

    if AdminChoise == "1":
        return customerRegistration()
    elif AdminChoise == "2":
        return EditRepeatFunc()
    elif AdminChoise == "3":
        return accountstatement()
    else:
        print("Invalid input")
        return adminchoise()


def customerid():  # get a account id in sequence
    CusFile = open("customerinfo.txt", "r")
    CusRawData = CusFile.readlines()
    CusFile.close()
    data = []
    n = 0
    for record in CusRawData:
        n += 1  # increase as a new line is read
        CusNewData = record.strip().split("\t")
        data.append(CusNewData)
    n += 1  # provide a new id when all line is read
    return n, data


def customerRegistration():  # allow user to enter data
    while True:
        n, data = customerid()
        n = str(n)
        Customerlist = []
        CustomerName = input("Enter Customer name: ")
        CustomerUsername = input("Enter Customer account username: ")
        CustomerId = input("Enter customer Id: ")
        Customeraddress = input("Enter customer address: ")
        CustomerGender = input("Enter customer Gender: ")
        CustomerDOB = input("Enter customer date of birth: ")
        CustomerPhone = input("Enter customer phone number: ")
        while True:  # only allow user to enter saving or current account
            CustomerSavingorCurrent = input("Enter customer wanted a saving or current account: ")
            CustomerSavingorCurrent = CustomerSavingorCurrent.lower()
            if CustomerSavingorCurrent == "saving" or CustomerSavingorCurrent == "current":
                break
            else:
                print("Invalid input\nPlease enter saving or current")
                continue
        for searchdata in data:  # validate customer can only have 1 current account
            filecustname = searchdata[1]
            filecustSoC = searchdata[2]
            if filecustname == CustomerName and filecustSoC == "current":
                print("Customer can only have 1 current account")
                break
            else:
                continue
        while True:
            try:
                Customerbalance = int(input("Enter amount of money customer entered: "))
                Customerbalance = str(Customerbalance)
                break
            except ValueError:
                print("Please enter numbers only")
                continue
        password = CustomerName + CustomerDOB
        Customerlist.append(n)
        Customerlist.append(password)
        Customerlist.append(CustomerSavingorCurrent)
        Customerlist.append(Customerbalance)
        Customerlist.append(CustomerName)
        Customerlist.append(CustomerGender)
        Customerlist.append(CustomerDOB)
        Customerlist.append(Customeraddress)
        Customerlist.append(CustomerPhone)
        Customerlist.append(CustomerId)
        Customerlist.append(CustomerUsername)
        Clist = "\t".join(Customerlist)
        WCust = open("customerinfo.txt", "a")
        WCust.write(Clist)
        WCust.write("\n")
        WCust.close()
        while True:
            cont = input("Enter 1 to continue\nEnter 2 to Stop editing: ")
            if cont == "1":
                break
            elif cont == "2":
                return
            else:
                print("Invalid input")
                continue


def choiseEditCustomer():
    FCust = open("customerinfo.txt", "r")
    customerUserId = input("Enter Customer Username: ")
    customerpassword = input("Enter Customer password: ")
    CusRawData = FCust.readlines()
    CusList = []
    num = -1  # to identify which line of data is used
    for record in CusRawData:
        CusNewData = record.strip().split("\t")  # split the string into a list base on \t and strip \n
        CusList.append(CusNewData)  # list is stored into a variable
    FCust.close()
    for CustomerSearchData in CusList:
        num += 1
        FileCustomerusername = CustomerSearchData[10]
        FileCustomerPassword = CustomerSearchData[1]

        if customerUserId == FileCustomerusername and customerpassword == FileCustomerPassword:  # validation
            while True:
                try:
                    editchoise = int(input("Enter 1 to change customer gender: \nEnter 2 to change customer date of birth: \nEnter 3 to change customer "
                                           "address: \nEnter 4 to change phone number: \nEnter 5 to change customer balance: \nEnter 6 to change customer "
                                           "username"))
                except ValueError:
                    print("Invalid Input")
                    continue

                if editchoise == 1:
                    choises = "Gender"
                    NEdit = 4
                    return num, NEdit, CusList, choises

                elif editchoise == 2:
                    choises = "Date of birth"
                    NEdit = 6
                    return num, NEdit, CusList, choises

                elif editchoise == 3:
                    choises = "Address"
                    NEdit = 7
                    return num, NEdit, CusList, choises

                elif editchoise == 4:
                    choises = "Phone number"
                    NEdit = 8
                    return num, NEdit, CusList, choises

                elif editchoise == 5:
                    choises = "Balance"
                    NEdit = 5
                    return num, NEdit, CusList, choises
                elif editchoise == 6:
                    choises = "Username"
                    NEdit = 10
                    return num, NEdit, CusList, choises

                else:
                    continue
        else:
            continue
    while True:
        print("Invalid input")
        ContinueorQuit = input("Enter 1 to continue: \nEnter 2 to quit: ")
        if ContinueorQuit == "1":
            return EditRepeatFunc()
        elif ContinueorQuit == "2":
            quit()
        else:
            print("Invalid Input")
            continue


def EditRepeatFunc():
    num, NEdit, CusList, choises = choiseEditCustomer()
    FCust = open("customerinfo.txt", "r")
    print("Enter new Customer ", choises, ": ")
    editCustBal = input("")
    newlist = CusList[num]
    newlist[NEdit] = editCustBal
    newlist = "\t".join(newlist)
    data = FCust.readlines()
    data[num] = newlist + "\n"
    FCust.close()

    WCust = open("customerinfo.txt", "w")
    WCust.writelines(data)
    WCust.close()
    while True:  # to let user know they want to continue editing
        COQ = input("Enter 1 to continue editing: \nEnter 2 to stop editing: ")
        if COQ == "1":
            return EditRepeatFunc()
        elif COQ == "2":
            break
        else:
            print("invalid input")
            continue
    return


def accountstatement():
    FCust = open("customerinfo.txt", "r")
    customerUserId = input("Enter Customer Username: ")
    customerpassword = input("Enter Customer password: ")
    CusRawData = FCust.readlines()
    CusList = []
    for record in CusRawData:
        CusNewData = record.strip().split("\t")
        CusList.append(CusNewData)
    FCust.close()
    for CustomerSearchData in CusList:
        FileCustomerusername = CustomerSearchData[10]
        FileCustomerPassword = CustomerSearchData[1]
        FileCustomerID = CustomerSearchData[0]

        if customerUserId == FileCustomerusername and customerpassword == FileCustomerPassword:
            while True:
                startdate = input("Enter start date for account statement (format:dd/mm/yyyy): ")
                enddate = input("Enter end date for account statement (format:dd/mm/yyyy): ")
                try:  # make sure user entered date format is correct
                    datetime.strptime(startdate, "%d/%m/%Y")
                    datetime.strptime(enddate, '%d/%m/%Y')
                except ValueError:
                    print("Invalid input please enter date format (dd/mm/yyyy)")
                    continue
                else:
                    break
            Startdate = datetime.strptime(startdate, '%d/%m/%Y')  # convert string into datetime
            Enddate = datetime.strptime(enddate, '%d/%m/%Y')
            FList = open("listofDandW.txt", "r")
            ListRawData = FList.readlines()
            FileList = []
            for record in ListRawData:
                ListNewData = record.strip().split("\t")
                FileList.append(ListNewData)
            FCust.close()
            print("Account Statement from ", startdate, " to ", enddate, "in the sequence of \nDate of Transaction, Balance, Withdraw, Deposit, "
                                                                         "New Balance")
            for searchdate in FileList:
                FileDate = searchdate[1]
                FileAccNum = searchdate[0]
                FileDate = datetime.strptime(FileDate, '%d-%b-%Y')  # change into datetime to do comparision and validate
                if Startdate <= FileDate <= Enddate and FileAccNum == FileCustomerID:
                    AccState = searchdate[1:6]  # slice list to input specific index of the list
                    AccState = "\t".join(AccState)
                    print(AccState)
            return
        else:
            continue
    print("invalid input")
    return accountstatement()


# --------------------------------------------------------------------------------------------------------------------------------------------------
def customerlogin():
    customerUserId = input("Enter Your User Id: ")
    customerpassword = input("Ener your password: ")

    f = open("customerinfo.txt", "r")
    CusRawData = f.readlines()
    CusList = []

    for record in CusRawData:
        CusNewData = record.strip().split("\t")
        CusList.append(CusNewData)
    f.close()
    n = -1  # use to allocate user account data in other functions
    for CustomerSearchData in CusList:
        FileCustomerId = CustomerSearchData[10]
        FileCustomerPassword = CustomerSearchData[1]
        FileCustomerName = CustomerSearchData[4]
        FileCustomerSoC = CustomerSearchData[2]
        n += 1
        if customerUserId == FileCustomerId and customerpassword == FileCustomerPassword:
            print("Welcome ", FileCustomerName)
            while True:
                customerSoC = input("Enter Saving or Current account")
                customerSoC = customerSoC.lower()
                if FileCustomerSoC == customerSoC:
                    return CusList, n
                else:
                    print("invalid saving or current account")
                    continue
        else:
            continue
    print("Invalid input of user and password: ")
    while True:
        ContinueorQuit = input("Enter 1 to continue: \nEnter 2 to quit: ")
        if ContinueorQuit == "1":
            return customerlogin()
        elif ContinueorQuit == "2":
            quit()
        else:
            print("invalid input")
            continue


def storeaccountstatdata():
    RoW = input("Enter 1 to withdraw: \nEnter 2 to deposit: \nEnter 3 to change password\nEnter 4 to see transaction history")

    if RoW == "1":
        WithdrawAmount, newbal, accnum, CusBal = withdrawl()  # to store transaction history
        dep = "nil"
        WithdrawAmount = str(WithdrawAmount)
        Cusbal = str(CusBal)
        actstate = open("listofDandW.txt", "a")
        actdata = []
        currenttime = datetime.now()
        currenttime = currenttime.strftime("%d-%b-%Y")
        actdata.append(accnum)
        actdata.append(currenttime)
        actdata.append(Cusbal)
        actdata.append(WithdrawAmount)
        actdata.append(dep)
        actdata.append(newbal)
        for i in actdata:
            actstate.write(i)
            actstate.write("\t")
        actstate.write("\n")
        actstate.close()
        return
    elif RoW == "2":
        DepositeAmount, CusBal, accnum, Dnewbal = deposit()
        wit = "nil"
        DepositeAmount = str(DepositeAmount)
        Cusbal = str(CusBal)
        actstate = open("listofDandW.txt", "a")
        actdata = []
        currenttime = datetime.now()
        currenttime = currenttime.strftime("%d-%b-%Y")
        actdata.append(accnum)
        actdata.append(currenttime)
        actdata.append(Cusbal)
        actdata.append(wit)
        actdata.append(DepositeAmount)
        actdata.append(Dnewbal)
        for i in actdata:
            actstate.write(i)
            actstate.write("\t")
        actstate.write("\n")
        actstate.close()
        return
    elif RoW == "3":
        CustList, n = customerlogin()
        newpass = input("Enter new password: ")
        newCustList = CustList[n]
        newCustList[1] = newpass
        newlist = "\t".join(newCustList)
        FCust = open("customerinfo.txt", "r")
        data = FCust.readlines()
        FCust.close()
        data[n] = newlist + "\n"
        WCust = open("customerinfo.txt", "w")
        WCust.writelines(data)
        WCust.close()
        return
    elif RoW == "4":
        return accountstatement()
    else:
        print("Invalid input")
        return storeaccountstatdata()


def withdrawl():
    CusList, n = customerlogin()  # call variable from customerlogin function
    newCusList = CusList[n]
    accnum = newCusList[0]
    SaveorCur = newCusList[2]
    CusBal = newCusList[3]
    CusBal = int(CusBal)

    FCust = open("customerinfo.txt", "r")
    while True:
        while True:
            try:  # accept integer only
                WithdrawAmount = int(input("Enter withdraw amount: "))
            except ValueError:
                print("Please Enter Number only")
                continue
            else:
                if WithdrawAmount > CusBal:
                    print("Balance is lower than withdrawl amount\nBalance: ", CusBal, "\nWithdraw amount: ", WithdrawAmount)
                    continue
                else:
                    break
        if CusBal >= WithdrawAmount and CusBal >= 500 and SaveorCur == "current":
            newbal = CusBal - WithdrawAmount
            print("WIthdraw succesful!\nBalance: ", CusBal, "\nWithdraw amount: ", WithdrawAmount, "\nFinal balance: ", newbal)
            newbal = str(newbal)
            newCusList[3] = newbal  # replace balance with the new balance
            newlist = "\t".join(newCusList)
            data = FCust.readlines()
            data[n] = newlist + "\n"
            Cusbal = str(CusBal)
            FCust.close()

            WCust = open("customerinfo.txt", "w")
            WCust.writelines(data)
            WCust.close()
            return WithdrawAmount, newbal, accnum, Cusbal
        elif CusBal >= WithdrawAmount and CusBal >= 100 and SaveorCur == "saving":
            newbal = CusBal - WithdrawAmount
            print("WIthdraw succesful!\nBalance: ", CusBal, "\nWithdraw amount: ", WithdrawAmount, "\nFinal balance: ", newbal)
            newbal = str(newbal)
            newCusList[3] = newbal  # replace balance with the new balance
            newlist = "\t".join(newCusList)
            data = FCust.readlines()
            data[n] = newlist + "\n"
            Cusbal = str(CusBal)
            FCust.close()

            WCust = open("customerinfo.txt", "w")
            WCust.writelines(data)
            WCust.close()
            return WithdrawAmount, newbal, accnum, Cusbal
        else:
            print("Invalid Input please do not enter number less than your balance or minimum balance (saving RM100, current RM500)")
            continue


def deposit():
    CusList, n = customerlogin()  # call variable from customerlogin function
    newCusList = CusList[n]
    accnum = newCusList[0]
    CusBal = newCusList[3]
    CusBal = int(CusBal)
    RCust = open("customerinfo.txt", "r")
    while True:
        while True:
            try:
                DepositeAmount = int(input("Enter deposit amount: "))
            except ValueError:
                print("Please Enter Number only")
                continue
            else:
                break
        if DepositeAmount >= 1:
            newbal = CusBal + DepositeAmount
            print("Deposit succesful!\nBalance: ", CusBal, "\nDeposit amount: ", DepositeAmount, "\nFinal balance: ", newbal)
            Dnewbal = str(newbal)
            newCusList[3] = Dnewbal  # replace balance with the new balance
            newlist = "\t".join(newCusList)
            data = RCust.readlines()
            data[n] = newlist + "\n"
            CusBal = str(CusBal)
            RCust.close()

            WCust = open("customerinfo.txt", "w")
            WCust.writelines(data)
            WCust.close()
            return DepositeAmount, CusBal, accnum, Dnewbal
        else:
            while True:
                print("Please enter number bigger than 0")
                cont = input("Enter 1 to continue\nEnter 2 to stop: ")
                if cont == "1":
                    break
                elif cont == "2":
                    return
                else:
                    print("Invalid input")
                    continue
            continue
    return


def menu():
    userinput = input("Enter number to choose which type of operation\n1. Super user login\n2. Admin login\n3. "
                      "Customer login: ")
    if userinput == "1":  # validate user correct entry
        return Superlogin()
    elif userinput == "2":
        return Adminlogin()
    elif userinput == "3":
        return storeaccountstatdata()
    else:
        print("invalid input")
        return menu()


menu()
