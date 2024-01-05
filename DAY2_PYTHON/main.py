#datatypes 

#Strings
# str = "Hello"
# print(str[0])
# print(str[4])


# #Integer
# print(123 + 456)

# #Float
# print(3.1452)

# #Boolean
# True
# False

# num_char = len(input("What is your Name? "))
# #show the datatype
# print(type(num_char))


# a = float(10)
# print(type(a))

# print(70 + float(100))
# print(str(70) + str(100))


#Question 1

# two_digit_number = input("Write a two digit number : ")

# sum = int(two_digit_number[0]) + int(two_digit_number[1])

# print(sum)


# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3


# PEMDAS
# ()
# **
# */
# +-

# print(3 * 3 + 3 / 3 - 3)


#Question 2 BMI

# height = float(input("Enter your Height in meter : "))
# weight = int(input("Enter your weight in kg : "))

# bmi = int(weight / (height * height))

# print(bmi)


#round() 
# print(round(2.66666, 2))


# score = 0
# #user scores a point
# score += 1
# score -= 1
# score *= 1
# score /= 1
# print(score)



# score = 0
# height = 1.8
# isWinning = True

# #f-String

# print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")



#Question 3

age = input("Enter your Age : ")

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")