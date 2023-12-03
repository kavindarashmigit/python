student=0
while student <=10:
  y=str(input("Enter Student Name : "))
  x=int(input("Enter Student Mark : "))
  
  student = student+1
  if x<=35:
    print("Student name :",y)
    print("Your Grade is 'F' Work Hard")
  elif x<=55:
    print("Student name :",y)
    print("Your Grade is 'S' Work Hard")
  elif x<=65:
    print("Student name :",y)
    print("Your Grade is 'C' Good")
  elif x<=75:
    print("Student name :",y)
    print("Your Grade is 'B' Very Good")
  elif x>75:
    print("Student name :",y)
    print("Your Grade is 'A' SUPPER ")
