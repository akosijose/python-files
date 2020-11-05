# loop idioms
def counting():
    zork = 0
    print("Before:", zork)
    count = [9, 41, 12, 3, 74, 15, "apple", "guava"]
    for thing in count:
        zork += 1
        print(f"{zork}.) {thing}")
    print(f"After: {zork}")

def nameInfo():
    name = input("What's your name? ")
    age = int(input("Your age? "))
    gender = input("Gender? ")
    print(f"Hi my name is {name}, I am {age} years of age {gender} ")

# nameInfo()

def filtering():
    print("Before")
    for value in [9, 41, 12, 3, 74, 15]:
        if value > 20:
            print("Larger number", value)
    print("After")

def findingSmall():
    small_so_far = -1
    print("Before", small_so_far)
    for the_num in [9, 41, 12, 3, 74, 15]:
        if the_num < small_so_far:
            small_so_far = the_num
        print(small_so_far, the_num)
    print("After", small_so_far)
findingSmall()

def findingSmallValue():
    smallest = None
    print("Before")
    for value in [9, 41, 12, 3, 74, 15]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print(smallest, value)
    print("After", smallest)
# findingSmallValue()