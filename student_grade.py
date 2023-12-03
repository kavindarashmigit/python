student=0
count=1
while student <=5:
  x=int(input("Enter Student Mark : "))
  
  student = student+1
  if (x>75):
    print("A")
  elif (65<x<75):
    print("B")
  elif (55<x<64):
    print("C")
  elif (45<x<54):
    print("S")
  else:
    print("F")
  count=count+1
