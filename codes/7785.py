import sys
input = sys.stdin.readline

st = set()
length = int(input())
for _ in range(length):
    Name,Status = input().strip().split()
    if Status == "enter":
        st.add(Name)
    else:
        st.remove(Name)



s = list(st)
s.sort(reverse=True)
for a in s:
    print(a)