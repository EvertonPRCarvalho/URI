i=0
while i==2:
    X=float(input())
    Y=float(input())
    if X<0 or X>10:
        print("nota invalida")
        break
    else:
        i+=1
    if Y>=0 and Y<10:
        i+=1
    else:
        print("nota invalida")
print("media = %.2f"%((X+Y)/2))
    
        
