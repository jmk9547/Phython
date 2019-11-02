hour = input('Enter hours : ')
h = float(hour)
rate = input('Input rate : ')
r = float(rate)

if h > 40 :
    p = r*40 + 1.5*r*(h-40)
else :
    p = r*h

print(p)