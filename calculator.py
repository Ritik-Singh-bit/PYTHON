a=int(input("enter a num  : "))
b=int(input("enter a num  : "))
print(" for additon press A  , for subtraction press B , for multiplication press C ,  for divide press D , for All operations Press O ")
c=input("code: ")
match c:
    case "A":
        print(a+b)
    case "B":
         print(a-b)
    case"C":
         print(a*b)    
    case "D" :
        print(a/b)
    case "O" :
        print(a+b,a-b,a*b,a/b)
    case default :
        print("wrong input")
