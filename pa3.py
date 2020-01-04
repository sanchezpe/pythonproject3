#ask user 1 for information
name1=input("Enter name of customer #1: ")
gallons1=eval(input("Enter gallons for customer #1: "))
question1=input("Is customer #1 residential or commercial? ")

print("------------------------------------------------------")

#aks user 2 for information
name2=input("Enter name of customer #2: ")
gallons2=eval(input("Enter gallons for customer #2: "))
question2=input("Is customer #2 residential or commercial? ")

#calculates cost for user 1
if question1=="residential":
   cost1=1.15*gallons1/1000
elif question1=="commercial":
   cost1=100+0.45*gallons1/1000

#calculates cost for user 2
if question2=="residential":
   cost2=1.15*gallons2/1000
elif question2=="commercial":
   cost2=100+0.45*gallons2/1000

   
print("------------------------------------------------------")
print()

#print output
print(format("Name",'14'),format("Type",'14'),format("Gallons",'14'),format("Charge",'14'))
print("------------------------------------------------------")
print(format(name1[0].upper()+name1[1:12],'14'),format(question1.upper(),'14'),format(gallons1,'7.0f'),format(cost1,'13.2f'))
print(format(name2[0].upper()+name2[1:12],'14'),format(question2.upper(),'14'),format(gallons2,'7.0f'),format(cost2,'13.2f'))
