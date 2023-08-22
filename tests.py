# def contains_duplicate(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] == nums[j]:
#                 return True

#             return False


# # Example usage:
# nums = [1, 2, 3, 1]
# result = contains_duplicate(nums)
# print(result)  # Output: True


# def selection_sort(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]

#     return nums


# def contains_duplicate(nums):
#     selection_sort(nums)
#     for i in range(0, len(nums)-1):
#         if nums[i] == nums[i + 1]:
#             return True
#     return False


# # Example usage:
# nums = [1, 2, 3, 1, 7, 3, 8, 5, 3]
# print(contains_duplicate(nums))
# result = contains_duplicate(nums)
# print(result)  # Output: True


# def selection_sort(nums):
#     n = len(nums)

#     for i in range(n-1):
#         min_index = i

#         for j in range(i+1, n):
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]

#     return nums


# def contains_duplicate(nums):
#     selection_sort(nums)
#     n = len(nums)

#     for i in range(0, n):
#         if nums[i] == nums[i+1]:
#             return True

#     return False


# nums = [5, 1, 4, 2, 7, 3, 3]

# print(selection_sort(nums))


# print(contains_duplicate(nums))


# def qsort(nums):
#     if len(nums) < 2:
#         return nums

#     else:
#         pivot = nums[0]
#         less = [i for i in nums[1:] if i <= pivot]

#         greater = [i for i in nums[1:] if i > pivot]

#         return qsort(less) + [pivot] + qsort(greater)


# def contains_duplicate(nums):
#     qsort(nums)

#     for i in range(len(nums)):
#         if nums[i] == nums[i+1]:
#             return True

#         return False


# nums = [1, 2, 3, 1]
# result = qsort(nums)
# print(result)


# def contains_duplicates(nums):
#     hashset = set()

#     for i in nums:
#         if i in hashset:
#             return True
#         hashset.add(i)
#     return False


# nums = [1, 2, 3, 1]
# result = contains_duplicates(nums)
# print(result)


# def is_anagram(string1):

#     for i in string1:
#         print(i)


# word = "lmao"

# is_anagram("lmao")


# def is_anagram(self, string1, string2):
#     self.string1 = len(string1)
#     self.string2 = len(string2)

#     for i in range(string1):
#         for j in range(string2):
#             if string1[i] == string2[j]:
#                 return True
#             return False


# word = "example"
# sorted_word = ''.join(sorted(word))
# print(sorted_word)


# def is_anagram(self, s, t):
#     if len(s) != len(t):
#         return False

#     sorted_s = ''.join(sorted(s))
#     sorted_t = ''.join(sorted(t))

#     if sorted_s == sorted_t:
#         return True
#     return False

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     countS, countT = {}, {}

#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countT[t[i]] = 1 + countT.get(t[i], 0)
#     print(countT)

#     for c in countS:
#         if countS[c] != countT.get(c, 0):
#             return False
#         print(countS[c])

#     return True


# is_anagram("johnny", "nnohjy")


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq, t_freq = {}, {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1

    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    if s_freq != t_freq:
        return False

    return True


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # Create a dictionary to store character frequencies for both strings
        s_freq = {}
        t_freq = {}

        # Count character frequencies in string s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        # Count character frequencies in string t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Compare the frequency dictionaries
        return s_freq == t_freq

        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0 )
        #     countT[t[i]] = 1 + countT.get(t[i],0 )

        # for j in countS:
        #     if countS[j] != countT.get(j, 0):
        #         return False
        # return True

        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))

        # if sorted_s == sorted_t:
        #     return True
        # return False


# def two_sum(target, num, list):
#     current_index = list[0]
#     n = len(list)

#     for i in range(n):
#        for j in range(i+1, n ):
#            if num[i] + num[j] == target:
#                return [i, j]

#         return []


def two_sum(nums, target):
    twoSum_dict = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in twoSum_dict:
            return [twoSum_dict[diff], index]

        twoSum_dict[value] = index

    return []
