count=1
sum=0
mark=[]

while (count<=10):
  marks=int(input("Enter Your Marks :"))
  mark.append(marks)
  sum=sum+marks
  count=count+1

maximum=max(mark)
minimum=min(mark)
average=sum/10

print("Minimum of the Mark :",minimum)
print("Maximum of the Mark :",maximum)
print("Avarage of the Mark :",average)
