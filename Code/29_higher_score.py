student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = int(0)
for c in student_scores:
    c = int(c)
    if c > highest:
        highest = c

print(f"The highest score in the class is: {highest}")
