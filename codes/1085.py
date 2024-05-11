x,y,w,h = map(int,input().split())

li = []

li.append(w-x)
li.append(h-y)
li.append(x)
li.append(y)
print(min(li))