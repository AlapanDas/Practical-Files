
def findMedianSortedArrays( nums1, nums2) :
    m=len(nums1)
    n=len(nums2)
    nums1.append(nums2)
    for i in range(m):
        for j in range(n):
            if (nums1[j]>nums1[j+1]):
                nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
    print(nums1[(len(nums1)//2)])
        

findMedianSortedArrays([1,2],[3])