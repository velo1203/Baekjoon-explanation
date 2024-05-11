num = int(input())

i = 2
for a in range(num):
    while True:
        if num % i == 0:
            num /= i
            print(i)
        else:
            break
    i += 1