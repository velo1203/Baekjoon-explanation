n = int(input())
count = 1
startidx = 1
endidx = 1
sum = 1
while endidx != n:
    if sum == n:
        count+=1
        endidx += 1
        sum += endidx
    elif sum> n:
        sum-= startidx
        startidx+=1
    else:
        endidx+=1
        sum+=endidx

print(count)