# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print('After', zork)

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)

# n = 0
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

# exercises 5.1
def findDone():
    num = 0
    tot = 0.0
    while True:
        sval = input("Enter a number: ")
        if sval == "done":
            break
        try:
            fval = float(sval)
        except:
            print("Invalid input")
            continue
        print(fval)  
        num += 1
        tot += fval
    print("All done")
    print(f"Total:{tot} Count:{num} Average:{tot/num}")
findDone()