class Solution(object):
    def twoSum(self, nums, target):
        # Why: Pair value with index for tracking
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()  # Why: Allows two-pointer search
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]  # Why: Return original indices
            elif curr < target:
                begin += 1  # Why: Need a bigger sum
            else:
                end -= 1  # Why: Need a smaller sum
