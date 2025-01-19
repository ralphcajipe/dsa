array = [64, 34, 25, 12, 22, 11, 90, 5]  # The array to sort

array_length = len(array) # Get the number of elements in the array

# Outer loop: We make n-1 passes to sort the array
for pass_num in range(array_length - 1):
    swapped = False # Flag to check if a swap happens in this pass
    
    # Inner loop: Compare near (adjacent) elements and swap if needed
    for index in range(array_length - pass_num - 1):
        if array[index] > array[index + 1]: # If the current element is greater than the next
            array[index], array[index + 1] = array[index + 1], array[index] # Swap
            swapped = True # Mark that a swap happened
    
    # If no swaps were made, exit the loop early
    if not swapped:
        break # Array is already sorted, no need for further passes
    
print(f"Sorted array: {array}")
