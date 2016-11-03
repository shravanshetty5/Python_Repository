def merge(low,high,array):
    i =0
    j =0
    k=0
    while(i<len(low) and j<len(high)):
        if low[i] < high[j]:
            array[k] = low[i]
            i += 1
            k += 1
        else:
            array[k] = high[j]
            j += 1
            k += 1
    while(i<len(low)):
        array[k] = low[i]
        i += 1
        k += 1
    while(j<len(high)):
        array[k] = high[j]
        j += 1
        k += 1




def mergeSort(array):
    n = len(array)
    count = 0
    if n > 1:
        low = array[:n/2]
        high = array[n/2:]
        mergeSort(low)
        mergeSort(high)
        merge(low,high,array)
if __name__ == "__main__":
    array = [10,2,7,5,28,22,12,7,8]
    print array
    mergeSort(array)
    print array
