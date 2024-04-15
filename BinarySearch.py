def BinarySearch(arr,low,high,key):
    if high<low:
        return None

    mid = (low+high)//2
    if key >arr[mid]:
        return BinarySearch(arr,mid+1,high,key)
    elif key<arr[mid]:
        return BinarySearch(arr,low,mid-1,key)
    else:
        return '该值下标为:%s,值为:%s'%(mid,arr[mid])

arr = input("请输入一组整数，用空格分隔: ")
arr1 = list(map(int, arr.split()))

arr1.sort()#确保数组有序
print("输入后的数组:" ,arr1)

key = int(input("请输入要查找编号的数字: "))
result=BinarySearch(arr1,0,len(arr1)-1,key)

if result is not None:
 print(result)
else:
 print("未找到该数字！") 