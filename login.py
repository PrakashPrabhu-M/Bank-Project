import random
def accno():
  try:
    no=int(input("Enter the name: "))
    return no
  except ValueError:
    print("Enter the correct number")
    return accno()

def name():
  na=input("Enter the name:")
  for i in na:
    if ord(i) not in range(65,123):
      print("Enter the correct name:") 
      return name()
  return na

def pin():
  try:
    pword=int(input("Enter the PIN no:"))
    return pword
  except ValueError:
    print("Enter the correct PIN number")
    return pin()

def withdrawl(T_am):
  try:
    w_amount=int(input("\nEnter the withdrawl amount:"))
    if T_am - w_amount <= 5000:
      print("Insuffient Account balance:")
      menu()
    else:
      T_am=T_am - w_amount
      details()
  except ValueError:
    print('Type an integer')
    return withdrawl()

def menu(dic):
  try:
    print("1.Withdrawl \n2.Deposit \n3.Show Details \n4.Ministatement")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
      withdrawl(dic)
    elif ch==2:
      deposit()
    elif ch==3:
      details()
    elif ch==4:
      mstatement()
    else:
      print("\nEnter the correct choice:")
      menu()

  except ValueError:
    print('Type an valid integer')
    menu()


def login():
  A_no=accno()
  P_name=name()
  pinno=pin()
  for i in range(usercount):
    if A_no in users[i].d.values() and P_name in users[i].d.values() and pinno in users[i].d.values():
      for i in range(usercount):
        if users[i].d['accno']==A_no:
          menu(users[i].d)
    else:
      print("Invalid account number or PIN ")

class initial:
  def create(self):
    d={}
    d['bal']=10000
    d['acc_id']=random.randint(1000000000000000,9999999999999999)
    print('ACCOUNT ID: {}'.format(d['acc_id']))
    namerun=True
    while namerun:
      namerun=False
      d['name']=input('Enter your name: ')
      if d['name'].strip()=='':
        print('Type something')
        namerun=True
        continue
      for i in d['name'].lower():
        if not 97<=ord(i)<=122:
          print('Enter a valid name (without numbers or symbols)')
          namerun=True
          continue
    
    pinrun=True
    while pinrun:
      pinrun=False
      try:
        d['PIN']=int(input('Type your own PIN number: '))
      except ValueError:
        print('Type numbers not characters')
        pinrun=True
        continue
      if d['PIN']<0:
        print('Enter a positive interger')
        pinrun=True
        continue

    passrun=True
    while passrun:
      passrun=False
      d['pass']=input('Type your Password: ')
      if len(d['pass'])<10:
        print('Password must atleast 10 characters long')
        passrun=True
        continue

    login()

users=[]
usercount=-1
beginrun=True
while beginrun:
  beginrun=False
  try:
    ch=int(input(('WELCOME'.center(50,'*')+'\nEnter your choice with numbers\n1.CREATE NEW ACCOUNT\n2.LOGIN\n')))
  except ValueError:
    print('Only numbers are allowed')
    beginrun=True
    continue
  if ch==1:
    usercount+=1
    users.append(initial())
    users[usercount].create()
  elif ch==2:
    login()
  else:
    print('Invalid choice')
    beginrun=True
    continue
