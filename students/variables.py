my_name = "Dominik"

print(my_name)

my_name = "Peter"

print(my_name)

player_1 = "Dominik"
player_2 = 'Peter'

welcome_message = "Hallo " + player_1 + " und " + player_2 + "!"

print(welcome_message)

number_1 = 5
number_2 = 10

# Addition
result_1 = number_1 + number_2

print(result_1)

# Subtraction
result_2 = number_1 - number_2

print(result_2)

# Multiplication
result_3 = number_1 * number_2

print(result_3)

# Division
result_4 = number_2 / number_1

print(result_4)

# Division by zero
# result_5 = number_1 / 0

# print(result_5)

# Lists

students = ["Peter", "Paul", "Marie"]

print(students)
print(students[1])

students.append("Lena")

print(students)

students.remove("Paul")

print(students)

del students[2]

print(students)

student_count = len(students)

print(student_count)

# Tuples

friends = ('Alex', 'Maximilian', 'Anna', 'Sarah')

print(friends)

# friends[0] = "Paul"

friend_count = len(friends)

print(friend_count)

contacts = [
    ["Anna", "Westermann", 16, "anna.westermann@gmail.com"],
    ["Paul", "Franke", 17, "paul.franke@gmail.com"]
]

print(contacts[0][1])

contacts = [
    {"firstname": "Anna", "lastname": "Westermann", "age": 16, "email": "anna.westermann@gmail.com"},
    {"firstname": "Paul", "lastname": "Franke", "age": 17, "email": "paul.franke@gmail.com"}
]

print(contacts[0]["firstname"])

del contacts[1]["age"]

print(contacts[1])
