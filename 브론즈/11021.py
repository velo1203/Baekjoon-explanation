testcase = int(input())
results = []
for n in range(testcase):
    a = input()
    (x,y) = map(int,a.split())
    results.append(f"Case #{n+1}: {x+y}")

for res in results:
    print(res)