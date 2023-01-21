import random

class Quicksort:

    def Quicksort(self, arr, left, right):
        if left < right:
            pivot = self.partition_pivot(arr, left, right)
            self.Quicksort(arr, left, pivot-1)
            self.Quicksort(arr, pivot+1, right)
        return arr
    
    def partition_pivot(self, arr, left, right):
        pivot = random.randint(left, right)
        arr[pivot], arr[right] = arr[right], arr[pivot]
        left_idx = left
        right_idx = right-1
        while left_idx <= right_idx:
            if arr[left_idx] <= arr[right]:
                left_idx+=1
            elif arr[right_idx] >= arr[right]:
                right_idx-=1
            else:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                left_idx+=1
                right_idx-=1

        arr[left_idx], arr[right] = arr[right], arr[left_idx]
        return left_idx
            
class main():
    nums = [4, 1, 6, 3, 5, 7, 2]
    left = 0
    right = len(nums)-1
    qs = Quicksort()
    sortedArr = qs.Quicksort(nums, left, right)
    print(sortedArr)
    