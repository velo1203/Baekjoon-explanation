def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value

res = min(1,3)
print("min" + res)