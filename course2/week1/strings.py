# using while loop
def _while():
    fruit = "banana"
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(index, letter)
        index += 1
# _while()

# using for loop
def _forloop():
    fruit = "banana"
    for letter in fruit:
        print(letter)
# _forloop()

# counting the letter using for loop
def countingLetter():
    word = "Jose Gerald Lumbao"
    count = 0
    for letter in word:
        if letter == "a":
            count += 1
    print(count)
countingLetter()