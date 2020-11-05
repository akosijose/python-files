# using in
def n1():
    fruit = "banana"
    pos = fruit.find("x")
    print(pos)

def n2():
    greet = "Hello Bob"
    new_greet = greet.replace("Bob", "Jose")
    print(greet)

def n3():
    _greet = "   Hello World!   "
    _greet.strip()

def n4():
    data = "From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"
    atpos = data.find("@")
    print(atpos)
    sppos = data.find(" ",atpos)
    print(sppos)
    host = data[atpos + 1 : sppos]
    print(host)


def Q1():
    str1 = "Hello"
    str2 = 'there'
    bob = str1 + str2
    print(bob)

# x = 'From marquard@uct.ac.za'
# print(x[14:17])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])