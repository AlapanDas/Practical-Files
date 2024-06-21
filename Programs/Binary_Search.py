def search(l,low,high,unit):
    if low>high:
        return -1
    mid=(low+high)//2
    if unit<l[mid]:
        high=mid-1
        return search(l,low,high,unit)
    elif unit>l[mid] :
        low=mid+1
        return search(l,low,high,unit)
    else:
        return mid
lst=[int(item) for item in input("Enter the Number ").split()]
unit=int(input("Enter item to search"))
ans=search(lst,0,len(lst)-1,unit)
if ans>=0:
    print("Found at index",ans)
else:
    print("Not found")
