import sys
input = sys.stdin.readline

txt = input().strip()
se = set()
length = len(txt)

for i in range(length):
    for j in range(i+1, length+1):
        se.add(txt[i:j])

print(len(se))
