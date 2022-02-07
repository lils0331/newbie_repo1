character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print ("he was 35 years old.")
print("He really liked the name " + character_name + ",")
print("35.")
character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("35.")


phrase = "Giraffe Academy"
print(phrase.index("Acad"))   #what number the letters in bracket start
print(phrase.replace("Giraffe","Elephant"))   #replacing one phrase with another

print(2)
print(3*(4+5))
print(10 % 3) #get the remainder

from math import * #give us access to alot more math function
my_num = 5
print(str(my_num)+ "my favorite number") #by adding str, you turn the number into a string
my_numb = 6
print(abs(my_numb)) #absolute value of a numnber
print(pow(3,2)) #3 power 2
print(max(4,6)) #which number is higher, or min for smallest number
print(round(3.7)) #round the number
print(floor(3.7)) #lower end of number
print(ceil(3.7)) #higher end of number
print(sqrt(3.7)) #sqrt of number

name = input("enter your name: ") #taking value user inputs storing it inside variable container called name
age = input("Enter your age:")
print("hello"+ name + "! you are " + age) #enter below a name and age, getting info from user input, interactive

#Calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2 #when get input from user, by default python thinks is string
result = int(num1) + int(num2) #convert both from string to intergers, whole numbers
result = float(num1) + float(num2) #convert both from string to decimal numbers
print(result)

#madlib game
color = input("Enter a color")
plural_noun = input("Enter a plural noun")
celebrity = input("Enter a celebrity")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

print("i love zhen")
