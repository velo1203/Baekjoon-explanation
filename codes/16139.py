import sys
input = sys.stdin.readline
t = input().strip()

ran = int(input())
for n in range(ran):
    txt, a,b = input().split()
    a,b = int(a),int(b)
    print(t[a:b+1].count(txt)) #hi