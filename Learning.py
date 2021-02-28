def computepay(h, r):
    if h>=40:
        total = ((h-40)*1.5*r)+(40*r)
        return total
    elif h<40:
        total = h*r
        return total

hrs = input("Enter Hours: ")
H=float(hrs)
rate = input("Enter rate: ")
R=float(rate)
p = computepay(H, R)
print("Pay", p)
s