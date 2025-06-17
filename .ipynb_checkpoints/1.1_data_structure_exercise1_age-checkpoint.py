
#Prompt the user to enter their age using the input() function and store it in a variable.
#Convert the user's input from a string to an integer using the int() function and store it in another variable.
#Add 10 to the user's age using the + operator and store the result in a third variable.
#Display the user's age after 10 years by printing the result.


#Variable called 'Age' Input to enter the age
#1 and #2
Age = int(input('Enter the age:'))

#Second variable to add +10 in first variable
#3
age1 = Age+10

#4
#Print variable 2
#4.1 Print with ,
print('The age is: ',  age1)

#4.2 Print with f ''
print(f'Your age is: {age1}')



#If someone add the number in letters
age_letters= input('Please enter the age:')
try: 
    age_converted = int(age_letters)
    age_converted1= age_converted + 10
    print('The age is: ' , age_converted1)
except:
    print('Please enter only digits')





