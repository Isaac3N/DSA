# from collections import defaultdict

# city_map = defaultdict(list)

# canada_cities = ["Vancouver", "Toronto", "Calgary"]

# nigerian_cities = ["Lagos", "Abuja", "Abia"]

# us_cities = ["washington", "chicago", "virginia"]

# city_map["Canada"] += canada_cities

# city_map["Nigeria"] += nigerian_cities

# city_map["USA"] += us_cities

# print(city_map.keys())


# for x in range(3):
#     print(x)

# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]

# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)


arr = ["bob", "alice", "jane", "doe"]


arr.sort(key=lambda x: len(x))

arr.reverse()


print(arr)
