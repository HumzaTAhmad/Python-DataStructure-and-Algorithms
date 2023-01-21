#Things to remember:
# -Don't forget to initialze pivot to the value of arr[right]
# -Don't forget to swap arr[right] to the positoin of the arr[left_idx] this is where the pivot is in the correct spot

import random

class QuickSort:
        
    def quicksort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quicksort(nums, left, pivot - 1)
            self.quicksort(nums, pivot + 1, right)
        return nums
        
    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        
        left_index = left
        right_index = right-1
        while left_index <= right_index:
            if nums[left_index] <= pivot:
                left_index+=1
            elif nums[right_index] >= pivot:
                right_index-=1
            else:
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                left_index+=1
                right_index-=1
        
        nums[left_index], nums[right] = nums[right], nums[left_index]
        return left_index
        

class main:
    qs = QuickSort()
    arr = [2, 6, 3, 9, 8, 5]
    left = 0
    right = len(arr)-1
    sorted_arr = qs.quicksort(arr, left, right)
    print(sorted_arr)