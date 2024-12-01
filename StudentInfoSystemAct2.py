idNumber = []
fullName = []
birthdate = []
gender = []
address = []

control = True

while control:
    print("----------------------------")
    print("EXAM INFORMATION SYSTEM")
    print("----------------------------")
    print("[A]. Add")
    print("[D]. Delete")
    print("[U]. Update")
    print("[S]. Show/Display")
    print("[E]. Exit")
    option = input("Enter Option: ").strip().upper()

    if option == "A":
        inpID = input("ID Number: ").strip()
        inpFname = input("Full name: ").strip()
        inpBday = input("Birth date: ").strip()
        inpGender = input("Gender: ").strip()
        inpAdd = input("Address: ").strip()
       
        idNumber.append(inpID)
        fullName.append(inpFname)
        birthdate.append(inpBday)
        gender.append(inpGender)
        address.append(inpAdd)
    elif option == "D":
        inpDel = input("Enter ID Number to Delete: ").strip()
        if inpDel in idNumber:
            delIndex = idNumber.index(inpDel)
      
            idNumber.pop(delIndex)
            fullName.pop(delIndex)
            birthdate.pop(delIndex)
            gender.pop(delIndex)
            address.pop(delIndex)
            print("Delete Successfully.")
        else:
            print("ID Number not found.")
    elif option == "U":
        inpUpdate = input("Enter ID Number to Update: ").strip()
        if inpUpdate in idNumber:
            updateIndex = idNumber.index(inpUpdate)
           
            fullName[updateIndex] = input("Full name: ").strip()
            birthdate[updateIndex] = input("Birth date: ").strip()
            gender[updateIndex] = input("Gender: ").strip()
            address[updateIndex] = input("Address: ").strip()
            print("Update Successfully.")
        else:
            print("ID Number not found.")
    elif option == "S":
        if idNumber:
            for i in range(len(idNumber)):
                print(f"ID NUMBER: {idNumber[i]} | FULL NAME: {fullName[i]} | BIRTH DATE: {birthdate[i]} | GENDER: {gender[i]} | ADDRESS: {address[i]}")
        else:
            print("No records to display.")
    elif option == "E":
        control = False
        print("Exiting.......")
    else:
        print("Invalid option. Please try again.")
