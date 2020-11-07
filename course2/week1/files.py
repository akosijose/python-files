# read the file using the open() function
# file = open("word.txt","r")
# count = 0
# for read in file:
#     count += 1
#     print("Line count", count)

file = open("word.txt")
print(file.read())