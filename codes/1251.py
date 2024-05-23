import sys
input = sys.stdin.readline

txt = input().strip()

length = len(txt)

t = []

for idx in range(1,length-1):
    for ix in range(idx+1,length):
        a = txt[:idx][::-1]
        b =txt[idx:ix][::-1]
        c = txt[ix:][::-1]
        t.append(a + b +c)
t.sort()
print(t[0])