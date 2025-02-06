import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
          'p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']

Digits=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','%','@','$','(','%','#','&','*',')']
print("Welcome to password Generator")
length=int(input("Enter the length of the password : "))
n_letters=int(input("Enter number of letters : "))
n_Digits=int(input("Enter number of digits required in your password: "))
n_symbols=int(input("Enter number of symbols required in your password:"))
if(n_letters+n_Digits+n_symbols!=length):
 print(f"Warning:The sum of letters,Digits,numbers doesn't match the desired length {length}")
 print(f"adjusting the desired length to {n_letters+n_Digits+n_symbols}")
password_list=[]
for i in range(1,n_letters+1):
      char=random.choice(letters)
      password_list+=char
for i in range(1,n_Digits+1):
      char= random.choice(Digits)
      password_list+=char

for i in range(1,n_symbols+1):
      char=random.choice(symbols)
      password_list+=char

print(password_list)
random.shuffle(password_list)
password=""
for i in password_list:
    password=password+i
print(password)
