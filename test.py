class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = []
        avg_nums = []
        n = len(nums)

        for i in range(n):
            l, r = i-k, i+k
            if l >= 0 and r < n:
                averages.append(nums[i])

                while l < i:
                    averages.append(nums[l])
                    l += 1
                while r > i:
                    averages.append(nums[r])
                    r -= 1
                average_index = sum(averages)//(k*2 + 1)
                avg_nums.append(average_index)

                averages.clear()
            else:
                avg_nums.append(-1)

        return avg_nums
