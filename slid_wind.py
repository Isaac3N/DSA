class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        char_set = set()
        counts = []
        count = 0
        print(len(s))

        while r < len(s):
            if s[r] in char_set:
                counts.append(count)
                count = 0

                char_set.clear()
                l += 1

            else:
                if len(s) == 1 or r == len(s)-1:
                    counts.append(count)
                char_set.add(s[r])
                count += 1
                print("count", count)
                r += 1

        print(len(char_set))
        print(char_set)
        print("counts", counts)
        print("count", count)

        if counts:
            max_count = max(counts)
            if max_count >= count:

                return max_count
            else:
                return count

        else:
            return 0


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, 0

        sum_val = nums[l]

        min_nums = 1000000

        while r < len(nums):
            if sum_val < target:
                r += 1
                if r < len(nums):
                    sum_val += nums[r]

            elif sum_val >= target:
                min_nums = min(min_nums, len(nums[l:r+1]))
                sum_val -= nums[l]
                l += 1

        if min_nums == 1000000:
            return 0

        else:
            return min_nums


my_list = {"a": 1, "b": 2, "c": 3}

maximum_value = max(my_list.values())
print(maximum_value)
