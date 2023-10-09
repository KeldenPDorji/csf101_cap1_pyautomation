# Function to calculate the maximum element in an array
def calculate_max(arr):
    max_value = arr[0]  # Initialize max_value with the first element
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

# Sample array
my_array = [1, 5, 2, 3, 4]

# Call the function to calculate the maximum element
result = calculate_max(my_array)

# Display the maximum element
print("The maximum element in the array is: {}".format(result))
