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

