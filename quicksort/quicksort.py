def partition(array, start, end):
    # Choose the last element as the pivot
    pivot_value = array[end]  # This is the pivot we're going to compare other elements against
    smaller_index = start - 1  # This keeps track of the position where the smaller elements should go

    # Loop through the array to find elements smaller than the pivot
    for current_index in range(start, end):  # Compare each element with the pivot value
        if array[current_index] <= pivot_value:  # If current element is smaller or equal to pivot
            smaller_index += 1  # Move the smaller_index forward
            # Swap to place the smaller element in its correct position
            array[smaller_index], array[current_index] = array[current_index], array[smaller_index]  

    # Place the pivot in its correct sorted position
    array[smaller_index + 1], array[end] = array[end], array[smaller_index + 1]  # Swap pivot with the element at smaller_index + 1
    return smaller_index + 1  # Return the index where the pivot is now placed


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1  # Set the end index to the last element if not provided

    if start < end:
        # Partition the array around the pivot, and get the pivot's final position
        pivot_position = partition(array, start, end)
        
        # Recursively apply quicksort on the left part (elements smaller than pivot)
        quicksort(array, start, pivot_position - 1)
        
        # Recursively apply quicksort on the right part (elements greater than pivot)
        quicksort(array, pivot_position + 1, end)


my_array = [64, 34, 25, 12, 22, 11, 90, 5] 
quicksort(my_array)  
print("Sorted array:", my_array) 
