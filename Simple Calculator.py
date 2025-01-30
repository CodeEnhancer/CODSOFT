# SIMPLE CALCULATOR
print(" Welcome to basic Calculator ")

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2   
def mod(num1,num2):
    return num1%num2
while(True):
      print("1= Addition")
      print("2=subtraction")
      print("3=Multiplication")
      print("4=Division")
      print("5=Remainder")
      option =int(input("Choose an operation: "))
      result=None

      if(option in [1,2,3,4,5]):
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))

      if(option==1):
            print(f"result=",round(add(num1,num2),2))
      elif(option==2):
            print(f"result= ",round(sub(num1,num2),2))
      elif(option==3):
            print(f"result=",round(mul(num1,num2),2))
      elif(option==4):
            print("result=",round(div(num1,num2),2))
      elif(option==5):
            print("result=",round(mod(num1,num2),2))
      else:
         print("Invalid operation entered")
         print(f"The result of the operation is {result}")
