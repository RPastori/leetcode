def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        if (target - nums[i]) in nums:
            if nums[i] != (target - nums[i]):
                return [i, nums.index(target - nums[i])]
            else:
                if nums.count(nums[i]) > 1:
                    return [i, (nums[:i]+nums[i+1:]).index(nums[i]) + 1]
