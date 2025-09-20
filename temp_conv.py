temp= float(input("enter temprature value :  "))
unit=input(" enter unit C/F/K :  ").upper()

if unit== "C":
    F= (temp*9/5) + 32 
    K = temp+ 273.15
    print(f"Temprature in Fahrenheit :{F : .2f}" )
    print(f"Temprature in Kelvin  :{K : .2f}" )
    
elif unit== "F":
      C= (temp-32)* 5/9
      K= (temp-32)*9/5+273.15
      print(f" Temprature in Celsius : { C :.2f}")
      print(f" Temprature in Kelvin  : { K :.2f}")
      
elif unit == "K":
     F= (temp- 273.15) * 9/5+ 32
     C= temp -273.15
     print(f"Temprature in Fahrenheit : {F : .2f}")
     print(f"Temprature in Celsius    : {C : .2f}")
     
else :
     print("Invalid unit! Please enter C, F, or K.")  
