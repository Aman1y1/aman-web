fruitsname=input("Enter the value:")
print(fruitsname)

if fruitsname==1:
    print("Apple")
elif fruitsname==2:
    print("Banana")
elif fruitsname==3:
    print("orange")
elif fruitsname==4:
    print("pineapple")
elif fruitsname==5:
    print("Mango")
elif fruitsname==6:
    print("grapes")


#else:
    #print("Invalid fruitsname:")

match fruitsname:
    case 1:
        print("Apple")
    case 2:
        print("Banana")
    case 3:
        print("Orange")
    case 4:
        print("pineapple")
    case 5:
        print("Mango")
    case 6:
        print("grapes")

   # case _:
         # print("Invalid fruit number")


