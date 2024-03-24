a = input()
(hour,minute) = map(int,a.split())
if minute - 45 < 0: 
    hour-= 1
    if hour < 0:
        hour = 23
    minute = 60 + (minute- 45)
else:
    minute -= 45

print(hour,minute)