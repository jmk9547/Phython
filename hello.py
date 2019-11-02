score = input("Enter Score: ")
fscore = float(score)
try :
    if fscore > 1.0 :
        print("Error") 
        quit()
    
    elif fscore < 0 :
        print("Error")
        quit()
except :
    print("Error")
    quit()
    
if fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")

#---------------------------------------------

#hour = input('Enter hours : ')
#h = float(hour)
#rate = input('Input rate : ')
#r = float(rate) 

#if h > 40 :
#    p = r*40 + 1.5*r*(h-40)
#else :
#    p = r*h

#print(p)

#---------------------------------------------
#def computepay(h,r):
#    if h > 40 :
#        p = (h-40)*1.5*r + 40*r
#    else :
#        p = r*h
#    return p

#rate = input("Enter rate = ")
#r = float(rate)
#hour = input("Enter hour = ")
#h = float(hour)

#p = computepay(h,r)
#print("Pay",p)


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
print("Pay",p)