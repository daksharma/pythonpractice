# This is a comment

world = "Hello World!"
print world
print (world[0:6])
print (world[6:12])
print (5 * 8)

PI = 3.14
print PI

# list can hold multipe value types
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print DAYS
print DAYS[3:7]

# number and day dictionary, Key : PairValue
# starting at 0 to 6, Sunday to Saturday
numAndDays = {}
for i in range(len(DAYS)):
    numAndDays[i] = DAYS[i]
print numAndDays


# Defining functions
def isPalindrone(word):
    word = word.replace(' ', '') #eliminate all spaces
    word = word.lower() #make everything lowercase
    # python ternary return result(truthy) if condition else falsey
    return "Palindrone" if word == word[::-1] else "Not Palindrone"
    # if word == word[::-1]:
    #     print("it is a palindrome")
    # else:
    #     print("it's not a palindrome")


print isPalindrone("racecar")
print isPalindrone("Too Bad I Hid A Boot")
print isPalindrone("hello dopeness")

