hour, minute = map(int, input().split())

minute = minute - 45

if minute < 0:
    hour -= 1
    minute = 60 + minute
    if hour < 0:
        hour = 23

print(hour, minute)
