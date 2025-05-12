def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
if __name__=="__main__":
    arr=[2,10,1,6,7,34,5]
    print(selection_sort(arr))
