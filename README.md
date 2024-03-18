# BinarySearch
二分查找-BinarySearch
def BinarySearch(arr,low,high,key):
    if high<low:
        return  
    mid = (low+high)//2
    if key >arr[mid]:
        low = mid +1
    elif key<arr[mid]:
        high = mid - 1
    else:
        return '该值下标为:%s,值为:%s'%(mid,arr[mid])
    return BinarySearch(arr,low,high,key)
 
arr = input("请输入一组整数，用空格分隔: ")
arr1 = list(map(int, arr.split()))

key = int(input("请输入要查找编号的数字: "))
result=BinarySearch(arr1,0,len(arr1)-1,key)

if result is not None:
    print(result)
else:
    print("未找到该数字！") 
