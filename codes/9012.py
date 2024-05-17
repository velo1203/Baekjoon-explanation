import sys
input = sys.stdin.readline

length = int(input())
for _ in range(length):
    stack = []
    txt = input().strip()
    for i,t in enumerate(txt):
        if t == "(":
            stack.append(t)
        else:
            if i == 0 and t ==")":
                stack.append(")") #강제예외
                break
            
            if len(stack) >= 1 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
    
    if len(stack) >= 1:
        print("NO")
    else:
        print("YES")