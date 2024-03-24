times = input()
(hour,minute) = map(int,times.split())

cooktime = int(input())

if (minute + cooktime) // 60 >= 1:
    hour += (minute+cooktime) // 60
    minute = (minute+cooktime) % 60
    if hour >= 24:
        hour = hour%24

else:
    minute += cooktime


print(hour,minute)