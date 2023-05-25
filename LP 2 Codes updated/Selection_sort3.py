def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the minimum element with the current element
    
    return arr
arr = [5, 2, 18, 12, 1]
sorted_arr = selection_sort(arr)
print(sorted_arr)