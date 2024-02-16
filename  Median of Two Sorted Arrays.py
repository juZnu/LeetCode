def median(array):
    if len(array) %2 :
        return array[len(array)//2]
    else:
        return (array[len(array)//2] + array[(len(array)//2)+1])/2
def findMedianSortedArrays( nums1, nums2):
    if len(nums1) < len(nums2):
        nums1,nums2 = nums2,nums1
    total = len(nums1)+ len(nums2)
    end1 = ((len(nums1)-1) //2) 
    end2 = (total//2) - end1 -2
    print(end1,end2)
    while nums1 and nums2:
        right1 =  nums1[end1+1] if  end1 +1< len(nums1) else float('inf')
        left1 = nums1[end1] if 0 <= end1 else float('-inf')
        right2=  nums2[end2+1] if end2+1 < len(nums2) else float('inf')
        left2 = nums2[end2] if 0 <= end2  else float('-inf')
        print(left1,right1)
        print(left2,right2)
        if left1 <= right2 and left2 <= right1:
            if total % 2 ==1:
                return min(right1,right2)
            else:
                return ( min(right1,right2) + min(max(left1,left2) , min(right1,right2)))/2
        elif left1 > right2:
            end1 -= 1
            end2 += 1
        else:
            end1 += 1
            end2 -= 1
    if nums1:
        return median(nums1)
    if nums2:
        return median(nums2)
print(findMedianSortedArrays(nums1 = [1,2,3,4,5,6], nums2 = [1,2,3,4,5,6]))
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [-1,3]))