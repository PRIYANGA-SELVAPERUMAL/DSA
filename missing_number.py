def find_missing_number(arr, n):
    
    expected_sum = n * (n + 1) // 2
   
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum


arr = [1, 2, 4, 5]
n = 5  
missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")
