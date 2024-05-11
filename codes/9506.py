import sys
input = sys.stdin.readline

while True:
    num = int(input())
    if num == -1:
        break
    li = []
    for n in range(1,num+1):
        if num % n == 0 and n != num:
            li.append(n)
    if sum(li) == num:
        print(f"{num} = ",end="")
        for i,a in enumerate(li):
            if i == len(li)-1:
                print(a)
            else:
                print(f"{a} + ",end="")
    else:
        print(f"{num} is NOT perfect.")