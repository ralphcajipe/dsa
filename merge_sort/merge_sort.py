def merge_sort(array):
    # If the array has 1 or no elements, it is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    middle_index = len(array) // 2
    left_part = array[:middle_index]  # Left half of the array
    right_part = array[middle_index:]  # Right half of the array

    # Recursively sort both halves
    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)

    # Merge the two sorted halves into a single sorted array
    return merge_sorted_arrays(sorted_left, sorted_right)

def merge_sorted_arrays(left_array, right_array):
    # Merges two sorted arrays into one sorted array
    merged_array = []
    left_index = 0
    right_index = 0

    # Compare elements from both arrays and add the smaller one to the merged array
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1

    # Add any remaining elements from the left array
    merged_array.extend(left_array[left_index:])

    # Add any remaining elements from the right array
    merged_array.extend(right_array[right_index:])

    return merged_array

# Example usage
unsorted_array = [3, 7, 6, -10, 15, 23.5, 55, -13]  
sorted_array = merge_sort(unsorted_array)  
print("Sorted array:", sorted_array) 
