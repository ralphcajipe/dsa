def binary_search(sorted_array, target_value):
    # Set the initial range of the search
    start_index = 0
    end_index = len(sorted_array) - 1

    # Continue searching while the range is valid
    while start_index <= end_index:
        # Calculate the middle index
        middle_index = (start_index + end_index) // 2

        # Check if the target value is at the middle index
        if sorted_array[middle_index] == target_value:
            return middle_index  # Target found, return its index

        # If the target is greater, narrow the search to the right half
        if sorted_array[middle_index] < target_value:
            start_index = middle_index + 1
        # If the target is smaller, narrow the search to the left half
        else:
            end_index = middle_index - 1

    return -1  # Target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Sorted array
target = 15  # Value to find

search_result = binary_search(numbers, target)

if search_result != -1:
    print(f"Value {target} found at index {search_result}.")
else:
    print(f"Value {target} not found in the array.")
