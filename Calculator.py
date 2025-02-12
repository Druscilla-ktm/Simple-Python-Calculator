num1=int(input("Enter first value: "))
num2=int(input("Enter Second value: "))

#store in list
hist1=[]
hist1.append(num1)
hist2=[]
hist2.append(num2)

#Choose Operation
operation=input("Enter Operation(+,-,*,/,h):")

if(operation=="+"):
       print(num1,"+",num2,"=",num1+num2)

elif(operation=="-"):
       print(num1,"-",num2,"=",num1-num2)

elif(operation=="*"):
       print(num1,"*",num2,"=",num1*num2)

elif(operation=="/"):
       print(num1,"/",num2,"=",num1/num2)

elif(operation=="h"):
#history
       print(hist1,operation,hist2)

else:
    print("Invalid Character")
