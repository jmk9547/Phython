def computepay(h,r):
    if h > 40 :
        p = (h-40)*1.5*r + 40*r
    else :
        p = r*h
    return p

rate = input("Enter rate = ")
r = float(rate)
hour = input("Enter hour = ")
h = float(hour)

p = computepay(h,r)
print(p)