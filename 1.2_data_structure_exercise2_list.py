#1 Create an empty list to store the grades.
grades = []
#  students = []

#2. Use the `input()` function to get the grade from the user for each student. Append each grade to the list
student1= float(input("Enter the grade for the 1 student: " ))
student2= float(input("Enter the grade for the 2 student: " ))
student3= float(input("Enter the grade for the 3 student: " ))
student4= float(input("Enter the grade for the 4 student: " ))
student5= float(input("Enter the grade for the 5 student: " ))


grades.append(student1)
grades.append(student2)
grades.append(student3)
grades.append(student4)
grades.append(student5)

#3. Calculate the average grade by summing up all the grades in the list and dividing by the number of grades.
aver = (student1+student2+student3+student4+student5)/len(grades)

#4. Display the average grade to the user.
print('The grades of the 5 students, are: ' , grades)
print('The average grade for the 5 students is: ', aver)