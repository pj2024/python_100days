import random
import my_module


# print(my_module.pi)

# random_number = random.randint(1, 10)
# print(random_number)
#
# random_float = random.random() * 5
# print(random_float)


# number = random.randint(1, 2);
#
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")


# states = [
#     "Alabama",
#     "Alaska",
#     "Arizona",
#     "Arkansas",
#     "California",
#     "Colorado",
#     "Connecticut",
#     "Delaware",
#     "Florida",
#     "Georgia",
#     "Hawaii",
#     "Idaho",
#     "Illinois",
#     "Indiana",
#     "Iowa",
#     "Kansas",
#     "Kentucky",
#     "Louisiana",
#     "Maine",
#     "Maryland",
#     "Massachusetts",
#     "Michigan",
#     "Minnesota",
#     "Mississippi",
#     "Missouri",
#     "Montana",
# ]

#for printing all items in the list
# print(states)

# for printing last items of the list
# print(states[-1])
# print(states[-2])

# for printing specific item of the list
# print(states[5])

# updating the list
# states[5] = "Maharashtra"
# print(states[5])


# add item to last of the list
# only one item added to the list with append() function
# states.append("Hingoli")
# print(states[-1])


# we can add multiple items with the help of extend() function
# states.extend(["Malegoan", "Shaapur"])
# print(states[-1])
# print(states[-2])
# print(states[-3])




# question to get a name from the list and then that person will pay the bill

# import random

# creating a list
# names_string = input("Enter names :")

# spliting the string and creating list
# names = names_string.split(", ")

# get total number of items in list
# num_item = len(names)

# generate random numbers between 0 to last index of list
# random_choice = random.randint(0, num_item - 1)

# person will pay the bill name
# person_will_pay_name = names[random_choice]

# print(f"{person_will_pay_name}  is going to pay the bill")

list1 = ['📦', '📦', '📦']
list2 = ['📦', '📦', '📦']
list3 = ['📦', '📦', '📦']

map = [
    list1,
    list2,
    list3
]

print(f"{list1}\n{list2}\n{list3}")
# print(map)
got_num = input("Where do you want to store the treasure 🥇 :").lower()

# print(got_num[0])
# print(got_num[1])
first_num = got_num[0]
abc = ["a", "b", "c"]

letter_index = abc.index(first_num)
# print(letter_index)
num_index = int(got_num[1]) - 1

map[num_index][letter_index] = '🥇'
#
print(f"{list1}\n{list2}\n{list3}")