import art
from replit import clear
print(art.logo)

# while(True):
#   firstnumber=float(input("what is your first number?"))
#   operator=input("choose an operator:\n+\n-\n/\n*\n\n")
#   secondnumber=float(input("what is your second number?"))
#   if operator=="+":
#     
#   elif operator=="-":
#     
#   elif operator=="/" :
#     
#   elif operator=="*":
#     
#   else:
#     print("Invalid operator")
#     break
#   proceed=input("Do you wish to do more calculations?y or n?") 
#   if proceed=='n':
#     break
#   clear() 



def add(a,b):
  return a+b

def sub(a,b):
  if a>b:
    return a-b
  else:
    return b-a

def multi(a,b):
  return a*b

def div(a,b):
  return a/b

# while(True):
#   n1=float(input("input first number"))
#   operator=input("Operator\n+\n-\n/\n*\n")
#   n2=float(input("input second number"))
#   if operator=="+":
#     print(add(n1,n2))
#   elif operator=="-":
#     print(sub(n1,n2))
#   elif operator=="*" :
#     print(multi(n1,n2))
#   elif operator=="/":
#     print(div(n1,n2))
#   else:
#     print("Invalid operator")
#     break
#   proceed=input("do you wish to proceed? y or n?")
#   if proceed=='n':
#     break
#   clear()  

# n1=float(input("input first number"))
# operator=input("Operator\n+\n-\n/\n*\n")
# n2=float(input("input second number"))
# cal=[
#   {
#     "value":multi,
#     "operator":'*',
#   },
#   {
#     "value":add,
#     "operator":'+',
#   },
#   {
#     "value":sub,
#     "operator":'-',
#   },
#   {
#     "value":div,
#     "operator":'/',
#   }
# ]

# for i in cal:
#   if operator==i["operator"]:
#     print(i["value"](n1,n2))
    
 
n1=float(input("input first number"))
operator=input("Operator\n+\n-\n/\n*\n")
n2=float(input("input second number"))

cal={
  "+":add,
  "-":sub,
  "*":multi,
  "/":div
}
for i in cal.keys():
  if operator==i:
    result=cal[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {cal[operator](n1,n2)}")

while True:
  proceed=input("Do you want to do more operation on the result? y or n?")
  if proceed=='n':
    print(f"final answer is {result}")
    break
  operator=input("Operator\n+\n-\n/\n*\n")
  second_num=float(input("What is the second number?"))
  
  n2=second_num
  n1=result
  for i in cal.keys():
    if operator==i:
      result=cal[operator](n1, n2)
      print(f"{n1} {operator} {n2} = {cal[operator](n1,n2)}")