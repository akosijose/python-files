num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        int_num = int(num)
    except :
        print('Invalid input')
        continue
    if smallest is None :
        smallest = int_num
    elif int_num < smallest :
        smallest = int_num
    elif int_num > largest :
        largest = int_num
print("Maximum is", largest)
print("Minimum is", smallest)