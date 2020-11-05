hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
if rate >= 40:
    a = rate * hrs
    b = (hrs - 40.0) * (a * 1.5)
    c = a + b
    print(c)

else:
    basic_rate = hrs * rate
    print('Pay:', str(basic_rate))
