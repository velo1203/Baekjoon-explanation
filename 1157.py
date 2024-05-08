import sys

input = sys.stdin.readline

txt = input().strip().upper()
txt_base = ''.join(set(txt))

txt_li = []
for n in txt_base:
    txt_li.append(txt.count(n))

if txt_li.count(max(txt_li)) > 1:
    print("?")
else:
    print(txt_base[txt_li.index(max(txt_li))])