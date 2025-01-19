def linear_search(array, target_value):
    for i in range(len(array)):
        if array[i] == target_value:
            print(f"Value {target_value} is found at index {i}")
            return i
    print(f"Value {target_value} is not found")
    return -1


array = arr = [3, 7, 2, 9, 5]
target_value = 7

result = linear_search(array, target_value)

# if result != -1:
#     print(f"Value {target_value} is found at index {result}")

# else:
#     print(print(f"Value {target_value} is not found"))
