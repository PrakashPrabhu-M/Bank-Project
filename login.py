def accno():
  try:
    no=int(intput("Enter the name:"))
    return no
  except TypeError:
    print("Enter the correct number")
    accno()

def name():
  na=input("Enter the name:")
  for i in na:
    if ord(i) not in range(65,123):
      print("Enter the correct name:") 
      name()
  return na

def pas():
  try:
    pword=int(input("Enter the PIN no:"))
    return pword
  except TypeError:
    print("Enter the correct PIN number")
    pas()

def withdrawl(T_am):
  try:
    w_amount=int(input("\nEnter the withdrawl amount:"))

    if T_am - w_amount <= 5000:
      print("Insuffient Account balance:")
      menu()
    else:
      T_am=T_am - w_amount
      details()



def menu():
  try:
    print("1.Withdrawl \n 2.Deposit \n 3.Show Details \n 4.Ministatement")
    ch=int(input("\nEnter your choice:"))
    if ch==1:
      withdrawl()
    elif ch==2:
      deposit()
    elif ch==3:
      details()
    elif ch==4:
      mstatement()
    else:
      print("\nEnter the correct choice:")
      menu()


def login():
  A_no=accno()
  P_name=name()
  pin=pas()
  if A_no in d and P_name in d and pin in d:
    menu()
  else:
    print("Invalid account number or PIN ")
