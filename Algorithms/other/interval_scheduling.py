a = (0,3)
b = (1,3)
c = (0,5)
d = (3,6)
e = (4,7)
f = (3,9)
g = (5,10)
h = (8,10)
R = [d,e,a,b,c,g,h,f]
R.sort(key=lambda x: x[1])
#print(R) # now R is sorted with first finish time at the beginning.
A = []
print(R)


while R: # keep going while R still has elements
    (si, fi) = R[0]
    A.append((si,fi))
    R_tilde = R.copy()
    
    for each in R:
        (sj, fj) = each

        if sj < fi:
            R_tilde.remove(each)

    R = R_tilde.copy()


print(A)
    
