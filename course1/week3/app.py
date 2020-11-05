weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
#1pound = 0.45

if unit.upper() =="K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
else:
    print("Wrong Unit")
