import myclass
while True:
    userlen=int(input("Enter lenght: \n"))
    print(myclass.Getpass(userlen))
    userch=input("Again? (y,n)\n")
    if userch.lower() == "y" :
        continue
    elif userch.lower() == "n" :
        print("TNX :D \n")
        break
    else :
        print(":/")
