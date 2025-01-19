array = [64, 34, 25, 12, 22, 11, 90, 5]

array_length = len(array) # Get the number of elements in the array

for pass_num in range(array_length - 1): # Outer loop: Run n-1 passes
    for index in range(array_length - pass_num - 1): # Inner loop: Compare near (adjacent) elements
        if array[index] > array[index + 1]: # If the current element is greater than the next
            array[index], array[index + 1] = array[index + 1], array[index] # Swap them
        
print(f"Sorted array: {array}")