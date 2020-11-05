
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")

try:
    new_hrs = float(hrs)
    new_rate = float(rate)
except:
    print('Error, please enter numeric input!')
    quit()

if new_rate >= 40:
    a = new_hrs * new_rate
    b = (new_hrs - 40.0) * (a * 1.5)
    c = a + b
    print(c)

else:
    basic_rate = new_hrs * new_rate
    print('Pay:', str(basic_rate))
