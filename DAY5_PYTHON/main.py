# fruits = ["apple", "chiku", "banana"]

# for fruit in fruits:
#     print(fruit)


# Calculate the average heights of the students 

# student_height = input("Enter your heights: ").split()
# sum = 0
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])


# total_height = 0
# number_of_students  = 0
# for height in student_height:
#     total_height += height
#     number_of_students += 1
# print(f'Total height = {total_height}')
# print(f'The number of students = {number_of_students}')

# avg_height = round(total_height / number_of_students)
# print(f"The average height = {avg_height}")



# program for calculating the heighest score of students

# student_score = input("Enter the scores: ").split()

# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])

# heighest_score = 0
# for score in student_score:
#     if heighest_score < score:
#         heighest_score = score
    
# print(f"The heihest score in the class = {heighest_score}")






# print 1 to 100

# for number in range(1, 101):
#     print(number)


# sum of 1 to 100
# total = 0
# for number in range(1, 101):
#     total += number

# print(f"sum of number is : {total}")



# for printing even number sum of that user entered 
#method first 

# user_number = int(input("Enter number: "))
# total = 0
# for number in range(1 , user_number+1):
#     if number % 2 == 0:
#         total += number

# print(f"the sum of total even number in range {user_number} is : {total}")

# method second

# user_number = int(input("Enter number: "))
# total = 0
# for number in range(2, user_number+1, 2):
#     total += number

# print(f"the sum of total even number in range {user_number} is : {total}")





# FizzBuzz game
# target = 100
# for number in range(1, target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)