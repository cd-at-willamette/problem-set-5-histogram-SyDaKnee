############################################
# Name: Sydney.
# Collaborators: I worked alone.
# Estimate of time spent (hr): 1 1/2 hr ish.
############################################

from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    max_value = max(data) # Finds the largest number in the data input list.
    histogram = [0] * (max_value + 1) # Creates a list of 0's where the length is one greater than the largest number in the data list to store the frequency of which each number appears.
    for number in data: # Loops through each number in the data list.
        histogram[number] += 1 # Increments the count at the index corresponding to the number, which tracks how many times each number appears.
    return histogram # Returns the histogram.

#1b
def print_histogram(hist:list[int]) -> None:
    for i, count in enumerate(hist): # Loops through the histogram. The index represents the number and the count represents how much that number appears.
        print(f"{i}: {'*' * count}") # Prints the index followed by the number-frequency asterisks for each number.

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width, height) # Create a GWindow.
    bar_width = width // len(hist) # Calculates the width of the bar in correspondance to the size of the histogram.
    max_count = max(hist) # Finds the largest frequency count in the histogram and scales the bar height accordingly.

    def my_rect(x,y,w,h,color): 
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    for i, count in enumerate(hist): # Loops through the histogram.
        bar_height = (count / max_count) * height # Scales the height of the bar in accordance to its specific count frequency and the heighest count frequency.
        my_rect(i * bar_width, height - bar_height, bar_width, bar_height, "red") # Draws each rectangle (bar) at the accurate positioning in the window.

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) 
graph_histogram(hist, 400, 400)
