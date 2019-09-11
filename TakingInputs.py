#hello
#this is a comment

#This program will multiply two ints

#Input
#the input function returns what the user returns
#all inputs starts as strings
#to change the type, you "cast" it
name = input("Please input your name: ")
a = input("please input first number: ")
a = int(a) #self referencing assignment
b = input("please input second number: ")
b = int(b)
#Process
product = a * b 

#Output
print("hi, "+name)
print("the product of " + str(a) + " and " + str(b) + " is " + str(product))
