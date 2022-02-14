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

while guess != secret_word: #as long as user doesn't guess secret word, keep looping for response
    guess = input("enter guess: ")

print("You win!") # not below while, success message

