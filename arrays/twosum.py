# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.


def two_sum(nums, target):

    num_maps = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in num_maps:
            return [num_maps[diff], index]
        num_maps[diff] = index
    return []
