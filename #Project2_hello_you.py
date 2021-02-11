
#Project_2, Hello you



#ask user for their name
name=input("What's your name?: ")

#ask user for their age
age=input("What's your age?: ")

#ask user for their city
city=input("What's your city?: ")

#ask user for what they love to do
do=input("What you love to do?: ")

#create output text
logic="Hey! Your name is {}, You are {} years old, your are from {} and you love to do {} ."
output=logic.format(name,age,city,do)

#print output to user
print(output)


