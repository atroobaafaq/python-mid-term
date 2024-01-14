print("CALCULATOR")
num1=int(input("enter the value1: "))
num2=int(input("enter the value2: "))
print("press + for addition\npress - for subtraction\npress * for multiplication\npress /for division")
choice=input("enter the choice +-*/")
if choice=='+':
      print(num1+num2)
elif choice=='-':
    print(num1-num2)
elif choice=='*':
    print(num1*num2)    
elif choice=='/':
    print(num1/num2)
else:
    print("invalid choice")
  
         
