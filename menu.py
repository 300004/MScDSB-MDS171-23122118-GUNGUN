listNames=[]
def storeName(name):
    name=name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True
def printNames():
     print("*"*30)
     for name in listNames:
        print(name)
        print("*"*30)
for name in listNames:
    print(name)
    print("*"*30)
def searchName(name):
    name=name.strip().title()
    flag=False
    for item in listNames:
        if name==item:
            flag=True
            break
        if flag==True:
            print("Name exist in the list")
        else:
            print("Name not found")
while True:
    print("Menu options")
    print("*"*30)
    print("1.enter a Name")
    print("2.enter a name to be searched")
    print("3.List all Names")
    print("4.Exit")

    choice=int(input("Enter your choice:"))  
    if choice==1:
        userInp=input("enter a name:")
        retVal=storeName(userInp)
        if retVal==True:
            print("Name added successfully") 
        else:
            print("Name exit in the list") 
    elif choice==2:
        userInp=input("Enter any name to be searched:")
        searchName(userInp)
    elif choice==3:
        printNames()
    elif choice==4:
        exit()
    else:
        print("Invalid option")