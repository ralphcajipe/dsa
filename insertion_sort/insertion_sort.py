my_array = [64, 34, 25, 12, 22, 11, 90, 5]

array_length = len(my_array)

# Start from the second element and move towards the end
for current_position in range(1, array_length):
    value_to_insert = my_array[current_position]  # The value we want to insert in the sorted portion
    position_to_insert = current_position  # Start with the current position to insert the value
    
    # Move through the sorted portion and find the correct place for the value_to_insert
    for previous_position in range(current_position - 1, -1, -1):
        if my_array[previous_position] > value_to_insert:
            my_array[previous_position + 1] = my_array[previous_position]  # Move larger elements one position to the right
            position_to_insert = previous_position  # Update the insertion position
        else:
            break  # Stop once we find the correct position for value_to_insert

    # Place the value in its correct position
    my_array[position_to_insert] = value_to_insert

print("Sorted array:", my_array)
