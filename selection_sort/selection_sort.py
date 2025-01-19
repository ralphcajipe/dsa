array = [64, 34, 25, 12, 22, 11, 90, 5]

array_length = len(array)

# Start sorting the array from the beginning
for current_position in range(array_length):
    index_of_smallest_value = current_position # Assume the smallest value is at the current position
    
    # Look for the smallest value in the remaining unsorted portion of the array
    for next_position in range(current_position + 1, array_length):
        if array[next_position] < array[index_of_smallest_value]:
            index_of_smallest_value = next_position  # Update the index of the smallest value
    
    # Swap the current element with the smallest element found
    array[current_position], array[index_of_smallest_value], = array[index_of_smallest_value], array[current_position]
    

print(f"Sorted array: {array}")