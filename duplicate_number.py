def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

arr = [3, 1, 3, 4, 2]
print("Duplicate number is:", find_duplicate(arr))
