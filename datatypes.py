# DATA TYPES
# Data types are classification of of values,
# that tells a computer how the programmer intends
# the data to be interpreted.

# below are the demonstration of basic data types in python

# Boolean
numbers  = [1,2,3,4,5]
boolean1 = 5 in numbers
boolean2 = 10 in numbers

print(boolean1) # Returns True since we have 5 among the set of number
print(boolean2) # Returns False since we NOT have 10 among the set of number


# NUMBERS Datatypes with arithmetic operators
num1 = 10 ** 5 # the double ** an Exponentiation operator
num2 = 40 // 4 # Floor division
num3 =  40 / 4 # Division
print(num1)
print(num2)
print(num3)

# STRINGS: Anything enclosed within quotes
str1 = "Welcome "
str2 = "Emmnauel Okaiwele, "
str3 = "This is my Python programming class for beginners"
str4 = str1 + str2 + str3 # concatenation: combinning several strings together
print(str4)

# LIST: Store multiple items in a single variable and are changable
StatesInNigeria = ['Abia', 'Adamawa', 'Akwa Ibom', 'Anambra']
print(len(StatesInNigeria)) # Print statement used with len function to return the no of item.
print(StatesInNigeria)
StatesInNigeria.append('Bauchi') # The append() method appends "Bauchi" to the end of the list.
print(StatesInNigeria)
StatesInNigeria.insert(3, 'Edo') # The insert() method inserts Edo at the third index
print(StatesInNigeria)

# TUPLES: 
Cloud_Provider = ('Amazon Web Service', 'Google Cloud', 'Azure Cloud', 'SalesForce')
Provider_List = list(Cloud_Provider)
Provider_List.append('Jovehost Managed Cloud')
print(Provider_List)
print(Cloud_Provider)

# DICTIONARY
CloudSkill = {
    'Programmig' : 'Python, Bash Shell', 
    'Cloud Computing': 'AWS, GCP',
    }
print('Emmnauel Okaiwele knows ', CloudSkill)