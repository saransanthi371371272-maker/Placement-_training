def minAnd2ndMin(arr):
    n = len(arr)

   
    if n < 2:
        return [-1]

   
    first = float('inf')
    second = float('inf')

    
    for i in range(n):
      
        if arr[i] < first:
            second = first
            first = arr[i]

       
        elif arr[i] < second and arr[i] != first:
            second = arr[i]

   
    if second == float('inf'):
        return [-1]

    
    return [first, second]


if __name__ == "__main__":
    arr = [12, 25, 8, 55, 10, 33, 17, 11]
    res = minAnd2ndMin(arr)
    
    for x in res:
        print(x, end=' ')
    print()
