# print("Welcome to the rollercoster ! ")
# height = int(input("What is your height in cm? "))

# if height >= 120 : 
#     print("You can ride the rollercoster!")
# else: 
#     print("Sorry, you have to grow taller before you can ride. ")



# ODD or EVEN
#if else
# number = int(input("Enter a positive integer : "))

# if number % 2 == 0 : 
#     print(f"You entered this {number} is EVEN number.")
# else:
#     print(f"You entered this {number} is ODD number.")



#Nested if else
# print("Welcome to the rollercoster ! ")
# height = int(input("What is your height in cm? "))

# if height >= 120 : 
#     print("You can ride the rollercoster!")
#     age = int(input("ENter your age : "))
    
#     if age <= 18 : 
#         print("please pay $7.")
#     else:
#         print("please pay $12.")
# else: 
#     print("Sorry, you have to grow taller before you can ride. ")



#if / elseif/ else
# print("Welcome to the rollercoster ! ")
# height = int(input("What is your height in cm? "))

# if height >= 120 : 
#     print("You can ride the rollercoster!")
#     age = int(input("ENter your age : "))
    
#     if age < 12:
#         print("please pay $5.")
#     elif age <= 18: 
#         print("please pay $7.")
#     else:
#         print("please pay $12.")
# else: 
#     print("Sorry, you have to grow taller before you can ride. ")



#BMI calculator

# print("Welcome to BMI calculator. ")

# height = float(input("Enter your height in meters : "))
# weight = int(input("Enter your wight in kg : "))

# bmi = (weight / height * height)

# if bmi < 18.5 : 
#     print(f"your bmi is : {bmi}, you are under weight. ")
# elif bmi >= 18.5 or bmi < 25:
#     print(f"your bmi is : {bmi}, you have normal weight. ")
# elif bmi >= 25 or bmi < 30:
#     print(f"your bmi is : {bmi}, you are slightly overweight. ")
# elif bmi >= 30 or bmi < 35:
#     print(f"your bmi is : {bmi}, You are obese.")
# else:
#     print(f"your bmi is : {bmi}, you are clinically obese. ")



#Leap year

# print("Welcome to leap year program! ")

# year = int(input("Enter any year : "))

# if year % 4 == 0: 
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"This year {year} is a leap year.")
#         else:
#             print(f"This year {year} is a not leap year.")
#     else:
#          print(f"This year {year} is a leap year.")
# else:
#      print(f"This year {year} is not a leap year.")


#find total bill
# print("Welcome to the rollercoster ! ")
# height = int(input("What is your height in cm? "))
# bill = 0;
# if height >= 120 : 
#     print("You can ride the rollercoster!")
#     age = int(input("Enter your age : "))
#     if age < 12:
#        bill = 5
#        print("Childs tickets are $5.")
#     elif age <= 18:
#         bill = 7 
#         print("Youth's tickets are $7.")
#     else:
#         bill = 12
#         print("Adult's tickets are $12.")

#     want_photo = input("Do you want photo type 'Y' or 'N' ") 
#     if want_photo == "Y":
#         bill += 3
#         print(f"Your bill is ${bill}.")
#     else:
#         print(f"Your bill is ${bill}.")   
# else: 
#     print("Sorry, you have to grow taller before you can ride. ")




#pyton pizza deliveries

# print("Thank you for choosing python pizza deliveries! ")

# bill = 0;

# size = input("What size pizza do you want? (S, M or L): ")

# add_pepperoni = input("Do you want pepperoni ? (Y or N): ")

# extra_cheese = input("Do you want extra cheese? (Y or N): ")

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your bill is ${bill}.")



#Love calculator

print("The Love calculator is calculating your score...")

name1 = input("Enter first person's name : ")
name2 = input("Enter second person's name : ")

combined_name = name1 + name2
full_name = combined_name.lower()
print(full_name)

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

true = str(t+r+u+e)

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

love = str(l+o+v+e)

score = int(true+love)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alrigt together.")
else:
    print(f"Your score is {score}.")

