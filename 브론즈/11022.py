import sys
testcase = int(sys.stdin.readline())
for n in range(testcase):
    nums = sys.stdin.readline()
    (x,y) = map(int,nums.split())
    print(f"Case #{n+1}: {x} + {y} = {x+y}")