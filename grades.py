print("This program calculates the averages of five students' grades.\n\n")

# Define a list of tuples containing the student names and grades
students = []
for i in range(5):
    name = input(f"Insert student {i+1}'s name: ")
    grade = float(input(f"Insert {name}'s grade: "))
    students.append((name, grade))

# Calculate the average grade
total = sum([grade for name, grade in students])
average = total / len(students)

# Print the results
print(f"The class average for the five students is {average}.")
