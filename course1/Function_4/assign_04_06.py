# def computepay():
#     if fh >= 40:
#         reg = fr * fh
#         otp = (fh - 40.0) * (fr * 0.5)
#         xp = reg + otp
#     else:
#         xp = fh * fr
#     return xp
#
#     sh = input("Enter hours: ")
#     sr = input("Enter rate: ")
#     fh = float(sh)
#     fr = float(sr)
#     print("Pay:",xp)
# computepay()

def computepay(h,r):

    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours: ")
hr = float(hrs)
rphrs = input("Enter rate per hour: ")
rphr = float(rphrs)

p = computepay(hr,rphr)
print("Pay",p)
