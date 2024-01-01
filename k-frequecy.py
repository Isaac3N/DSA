def k_frequency(nums):

    if len(nums) < 2:
        return nums

    frequency_map = {}

    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    most_freq = sorted(frequency_map.values).reverse

    return most_freq[0]
