# finding the largest number
largest_num = -1
num = [9, 41, 12, 3, 74, 15]
print("Before", largest_num)
for i in num:
    if i > largest_num:
        largest_num = i
    print(largest_num, i)
print("After", largest_num)
