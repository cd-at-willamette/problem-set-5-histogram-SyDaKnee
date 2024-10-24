##################################################
# Name: Sydney.
# Collaborators: I worked alone.
# Estimate of time spent (hr): 1 1/2 hr ish.
##################################################

def is_magic_square(array:list[list[int]]) -> bool: # Takes a list of lists of integers and returns "True" or "False".
    a = len(array) # Stores the number of rows in the square matrix.
    if not all(len(row) == a for row in array): # Check if all the rows are the same length as the length of the array (a), 
        return False # if they are not return False because the square matric isn't valid. 
    
    target_sum = sum(array[0]) # Holds the sum of the first row.

    for row in array: # For each row in the array,
        if sum(row) != target_sum: # If any row's sum does not equal the target sum,
            return False # Return "False".
    
    for col in range(a): # For each column in the array,
        if sum(array[row][col] for row in range(a)) != target_sum: # If any column's sum does not equal the target sum,
            return False # Return "False".

    if sum(array[i][i] for i in range(a)) != target_sum: # If the sum of the top-left to bottom-right (diagonal) does not equal the target sum,
        return False # Return "False".
    
    if sum(array[i][a - i - 1] for i in range(a)) != target_sum: # If the sum of the top-right to bottom_left does not equal the target sum,
        return False # Return "False".
    
    return True # If none of these things are ture, return "True".

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))
