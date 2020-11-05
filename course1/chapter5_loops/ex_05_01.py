# loops and iteration
def loop():
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("Blast off")
    print(n)
# loop()

# break statement
def word():
    while True:
        line = input(">>> ")
        if line == "done":
            break
        print(line)
    print("Done!")
# word()
# break statement

# continue statement
def con():
    while True:
        _line = input(">>> ")
        if _line[0] == "#":
            continue
        if _line == "done" or _line == "Done":
            break
        print(_line)
    print("Done!")
con()
# continue statement
