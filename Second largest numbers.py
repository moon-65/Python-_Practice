numbers=(23, 42, 69, 12, 5)
largest =None
second_largest = None
for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or (num > second_largest and num != largest):
        second_largest = num
print("The second largest number is :", second_largest)