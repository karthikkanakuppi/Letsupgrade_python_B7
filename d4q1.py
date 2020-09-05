lower=1042000
upper=7026488265

for i in range(lower,upper+1):

    l=len(str(i))
    s=0
    t=i
    while t>0:
        d=t%10
        s+=d**l
        t//=10
    if i==s:
        print("The first armstrong number is ",s)
        
        break
