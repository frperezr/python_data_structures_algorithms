
def insertion_sort(nums):

    for i in range(0, len(nums)):

        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            swap(nums, j, j - 1)
            j = j - 1


    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

if __name__ == "__main__":

    nums = [1, 5, 3, 8, 10, 100, 4]
    print(insertion_sort(nums))
