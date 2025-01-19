my_array = [7, 12, 9, 4, 11]

lowest_value = my_array[0]

for number in my_array:
    if number < lowest_value:
        lowest_value = number

print(lowest_value)

# easy way
print(min(my_array))
