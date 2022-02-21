#List

friends = ["Kevin","Karen","Jim"] #store a list of value inside the list
print(friends[0]) #refer element by index, starts with 0, negative number index backwards
print(friends[1:]) #refer element for everyone after 1
print(friends[1:3]) #refer element from 1 to 3 not including 3
friends[1] = "Mike" #mofidy value of index 1 to something else
print(friends[1])

lucky_number = [4,6,13,15,15,18]
friends = ["kevin", "karen", "jim", "oscar", "Toby"]
friends.extend(lucky_number) #adding friends and lucky number list together
friends.append("Creed") #add another friend to friends list, add to end of the list
friends.insert(1, "sally") #add friend at index 1 to friends list
friends.remove("jim") #remove friend jim
friends.pop() #top of the list
print(friends.index("kevin")) #is kevin in the list?
print(friends.count("Jim")) #how many times is jim in the list?
friends.sort() #alphebetical order
friends.clear() #clear all
lucky_number.reverse() #reverse the list
friends2 = friends.copy() #copy the list of friends

#Tuples - type of data structure, container where we store different values, immutable can't change it

coordinates = [(4, 5),(6,7),(80,34)] #store data that can't be changed or mutated, for datasets
print(coordinates[0])

#Functions - collection of code that performs tasks

def say_hi(name):  #allcode that comes after this line will be inside our function, has to indent code
    print("Hello " + name + ", you are "+ str(age)) #these are all in the function

say_hi("Mike", "35") #parameter is information we give
say_hi("Steve", "70")

#Functions - return statement, we want information back

def cube(num):
    return num*num*num #get info back from a function, can't add any code after

result = cube(4) #stored info from the function
print(result)

#if statement

is_male = True #boolean variables
is_tall = True

if is_male or is_tall: #if this person is a mail or is tall
    print("You are a male or tall or both")
elif is_male and not(is_tall): #if this person is a male but short
    print("You are a short male")
elif not(is_male) and is_tall: #if this person is not male but tall
    print("You are not a male but are tall")
else: #if above is false, this would be displayed
    print("You are neither male or tall")
if is_male and is_tall: #both conditions have to meet
    print("You are a tall male")

#if statement and comparisons, can compare number, strings, booleans

def max_num(num1, num2, num3): #max numbers between these 3 numbers
    if num1 != num2 #if num1 is not the same as num 2
    if num1 >= num2 and num1>= num3: #if num 1 is bigger than 2 and 3
        return num1
    elif num2 >= num1 and num2 >= num3: #else if, num 2 is bigger than 1 and 3
        return num2
    else:      #if 1 and 2 are both not the biggest, then num 3 is biggest
        return num3
print(max_num(3,4,5))

#Build a better calculator

num1 = float(input("Enter first number: ")) #convert whatever user inputs into float, or else it's automatic string
op = (input("Enter operator: ") #operator, addition, etc
num2 = float(input("Enter second number: ")) #number

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

#dictionary, convert 3 digit month name to full month name, store key value pairs

monthConversions = {
    "Jan": "Janurary",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
}

print(monthConversions["Nov"]) #get full month
print(monthConversions.get("Luv")) #put in a key that doesn't map to dictionary, we get none
print(monthConversions.get("Luv","not a valid key")) #if can't find, would return not a valid key

#While loop
i = 1
while i <= 10: #condition, after every execution, comes back to check the condion, max 10
    print(i)
    i += 1 #automatically add 1 to i

print("Done with loop")

#build basic guessing game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit =3
out_of_guesses = False #tell us weather or not users are out of guesses

while guess != secret_word and not(out_of_guesses): #as long as user doesn't guess secret word, and still have guesses
    if guess_count < guess_limit: #are the guess counts less than limit?
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, you lose")
else:
    print("You win")

#For loop, loop through every element

friends = ["jim", "Karen", "Kevin"]
for friend in friends:       #specify a collection you wanna go over
    print(friend)
for index in range (10) #print out every number from 0-9
    print(index)
for index in range(3,10):
    print(index) #print out all numbers from 3-10, excluding 10
len(friends) #how many element is in the array, how many friends
for index in range(len(friends)):
    print(friends[index])

for index in range(5): #only first printed is first iteration, everything else is not first
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

#Exponent function

def raise_to_power(base_num, pow_num): #parameters in bracket, taking in base number and pow number
    result = 1 #define variable called result, store actual result of doing math
    for index in range (pow_num): #specificy for loop, loop through power number of times, from 0 not including power number
        result = result * base_num
    return result

print(raise_to_power(3,2))

#2D list and nested loop, create grid looking list inside python

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[2][1])
for row in number_grid:
   for col in row: # we want each individual element inside the array
       print(col)

#Build a translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeious": #checking if letter is inside the string
            if letter.isupper():
                translation = translation + "G"
            else translation = translation +"g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase")))

#Try except blog - try out entering something

try:
    value = 10/0
    number = int(input("Enter a number")) #enter whatever and will convert to integer
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

#reading files

employee_file = open(#"name of the file", "r") # I only want to read the file inside, "w" means I want to write the file, overwritting everything in existing file
 # "a" means I want to add new information to the file, "r+" I want to read and write
    for employee in employee_file.readlines():
        print(employee) #print out each line in the file

print(employee_file.readable()) #tell us whether or not we can read the file
print(employee_file.readline()) # read first line of the file
print(employee_file.readlines()[1])
employee_file.close()

#Writing to the file

employee_file = open ("employees.text","a") #appending is easy to mess up the file
employee_file = open("employees1.text","w") #write a new file
employee_file.write("Toby - Human Resources")
employee_file.write("\nkelly = customer service") #add it to a new line
employee_file.close()

#Modules and Pip, python file we can import to our current python file, including useful functions, etc

import #type name of the file that's useful
print(#file name. will show functions) importing functionality to your python file
#search up list of python modules on google, will show up, external python and some are built in, like lib on the side

#classes and objects, create own data types, made student data type
from Student import Student

student1 = Student("Jim", "Business", 3.1, False) #want to create a student object (instance of a class)

print(student1.name)

#multiple choice quizz in python

from Question import Question

question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) yellow\n(b) green\n\n",
    "what color are strawberries?\n(a) red\n(b) green\n\n"
]

questions = [
    Question(question_prompts[0], "a"), #use a class to model this
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

def run_test(questions): #loop through and get user to answer to make sure its right
    score = 0
    for question in questions: #for each question object in question array we wanna do something
        answer = input(question.prompt)
        if answer == question.answer: #check to see if student gave right answer
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)

#Object functions

student1 = Student("Oscar", "Accounting", 3.1)
student2 = student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll)) #is this student on honor roll?

#Inheritence

from chef import chef




