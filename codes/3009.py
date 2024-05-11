import sys
input = sys.stdin.readline

tx=[]
ty= []
for n in range(3):
    x,y= map(int,input().strip().split())
    if x in tx:
        tx.remove(x)
    else:
        tx.append(x)

    if y in ty:
        ty.remove(y)
    else:
        ty.append(y)
print(tx[0],ty[0])