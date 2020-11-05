hrs = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))
if rate >= 40:
    
    sal = 40 * rate + (hrs - 40) * 1.5 * rate
    print(sal)
   
else:
    basic_rate = hrs * rate
    print('Pay:', str(basic_rate))
