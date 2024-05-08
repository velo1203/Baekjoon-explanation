import sys
input = sys.stdin.readline

li = ["c=","c-","dz=","d-","lj","nj","s=","z="]
txt = input().strip()

total = 0
for l in li:
    total += txt.count(l)
    txt = txt.replace(l," ")

print(total + len(txt.replace(" ","")))