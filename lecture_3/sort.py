list_1=[8,4]
print(f"LIST!!!!!!!{list_1}")
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        print(f"L:{left}")
        right=nums[mid:]
        print(f"R:{right}")
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                print(f"L[i]{left[i]}")
                print(f"R[j]{right[j]}")
                nums[k]=left[i]
                print(f"N1!!!!!!!{nums}")
                i+=1
            else:
                print(f"L[i]{left[i]}")
                print(f"R[j]{right[j]}")
                nums[k]=right[j]
                print(f'N2!!!!!!!{nums}')
                j+=1
            k+=1
            print(f'NUMS!!!!!!!{nums}')
            
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1

merge_sort(list_1)
print(f"LIST!!!!!!!{list_1}")