hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
# fh = float(hrs)
# fr = float(rate)

if hrs >= 40:
    reg = hrs * rate
    otp = (hrs - 40.0) * (rate * 0.5)
    xp = reg + otp
    # print(xp)
    print('Pay',str(xp))
else:
    xp = hrs * rate
    print('Pay:', str(xp))
