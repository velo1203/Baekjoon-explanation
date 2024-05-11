import sys
input = sys.stdin.readline

while True:
    A,B = map(int,input().strip().split()) 
    if A == 0 and B == 0:
        break

    if A < B:
        if B%A != 0:
            print("neither")
        else:
            print('factor')
    else:
        if A%B != 0:
            print("neither")
        else:
            print("multiple")