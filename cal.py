def add(a,b):
  return a+b
  
def subtract(a,b):
  return a-b
  
def multiply(a,b):
  return a*b

def divide(a,b):
  try:
    return a/b
  except:
    print("float division by zero")
   
def power(a,b):
  return a^b
  
def remainder(a,b):
  return a%b  

def print_answer(a,b,operand,answer):
  print("\n",a,operand,b,"=",answer)
  
def select_op(choice):
  if choice=="#":
    pass
  elif choice=="$":
    pass
  elif choice=="+":
    print_answer(a,b,choice,add(a,b))
  elif choice=="-":
    print_answer(a,b,choice,subtract(a,b))  
  elif choice=="*":
    print_answer(a,b,choice,multiply(a,b))
  elif choice=="/":
    print_answer(a,b,choice,divide(a,b))
  elif choice=="^":
    print_answer(a,b,choice,power(a,b))
  elif choice=="%":
    print_answer(a,b,choice,remainder(a,b))
  else:
      print("Unrecognized operation")
      
while True:
  print("\n\nSelect operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  choice = input("\nEnter choice(+,-,*,/,^,%,#,$): ") 
  
  if choice=="#":
      print("Done. Terminating")
      quit()
  elif choice=="$":
      continue;
  elif(choice=="+"or choice=="-" or choice=="*" or choice=="/" or choice=="^" or choice=="%"):
      pass
  else:
      print("Unrecognized operation")
      continue
      
  try:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
  except:
    print("Not a valid number,please enter again")
 
  select_op(choice)