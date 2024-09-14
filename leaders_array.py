def find_leaders(arr):
    n = len(arr)
    res = []
    max_right = arr[-1]
    res.append(max_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            res.append(max_right)
    
    return res[::-1]

arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))
