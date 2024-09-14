def find_zero_sum_subarrays(arr):
    n = len(arr)
    res = []
    
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == 0:
                res.append((i, j))
    
    return res

arr = [1, 2, -3, 3, -1, 2]
print("Zero sum subarrays:", find_zero_sum_subarrays(arr))
