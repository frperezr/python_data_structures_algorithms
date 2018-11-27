# Divide & Conquer
def merge_sort(nums):

    # Divide

    if len(nums) == 1:
        return

    middle_index = len(nums) // 2

    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # Conquer

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i = i + 1
        else:
            nums[k] = right_half[j]
            j = j + 1

        k = k + 1

    while i < len(left_half):
        nums[k] = left_half[i]
        k = k + 1
        i = i + 1

    while j < len(right_half):
        nums[k] = right_half[j]
        k = k + 1
        j = j + 1

# Test

if __name__ == "__main__":

    nums = [2, 5, 4, -1, 0, 1]
    merge_sort(nums)
    print(nums)
