# 1.

def hw1_try1(a, b, c):
    return len([i for i in range(a, b) if i % c == 0])

def hw1_try2(a, b, c):
    return ((b + a % c) - a) // c if a % c != 0 or (a % c == 0 and b % c == 0) else ((b + a % c) - a) // c + 1

def hw1_try2_easy_version(a, b, c):
    if a % c != 0 or (a % c == 0 and b % c == 0):
        return ((b + a % c) - a) // c
    else:
        return ((b + a % c) - a) // c + 1

# ალგორითმი ნაპოვნი და ჩამოყალიბებულია hw1.png ფაილში
# test:
print(hw1_try1(1, 20, 2))
print(hw1_try2(1, 20, 2))
print(hw1_try2_easy_version(1, 20, 2))
print()
print(hw1_try1(12, 19, 3))
print(hw1_try2(12, 19, 3))
print(hw1_try2_easy_version(12, 19, 3))
print()
print(hw1_try1(2, 20, 2))
print(hw1_try2(2, 20, 2))
print(hw1_try2_easy_version(2, 20, 2))
print("\n")
print(hw1_try2_easy_version(20,40,11))
# ✔

# 2.

converter = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, 
    "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, 
    "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, 
    "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
}

def hw2_try1(num, b): # works from 2 to 35 Position systems and converts all to decimal
    num = str(num)
    nums1 = []
    nums2 = []

    if "." in num:
        num = num.split(".")
        part1 = num[0][::-1]
        part2 = num[1]

        for i in range(len(part1)):
            nums1.append(int(converter[part1[i]]) * (b ** i))

        for x in range(len(part2)):
            nums2.append(int(converter[part2[x]]) * (1 / b ** (x+1)))

        return sum(nums1 + nums2)
    else:
        num = num[::-1]
        for i in range(len(num)):
            nums1.append(int(converter[num[i]]) * (b ** i))

        return sum(nums1)

# def hw2_try2(num, b, target):
#     num = str(num)
#     nums1 = []
#     nums2 = []

#     if "." in num:
#         num = num.split(".")
#         part1 = num[0][::-1]
#         part2 = num[1]

#         for i in range(len(part1)):
#             nums1.append(int(converter[part1[i]]) * (2 ** i))

#         for x in range(len(part2)):
#             nums2.append(int(converter[part2[x]]) * (1 / 2 ** (x+1)))

#         return sum(nums1 + nums2)
#     else:
#         num = num[::-1]
#         for i in range(len(num)):
#             nums1.append(int(converter[num[i]]) * (2 ** i))

#     result = sum(nums1)

#     result = str(result)
#     nums1 = []
#     nums2 = []

#     if "." in num:
#         num = num.split(".")
#         part1 = num[0][::-1]
#         part2 = num[1]

#         for i in range(len(part1)):
#             nums1.append(int(converter[part1[i]]) * (target ** i))

#         for x in range(len(part2)):
#             nums2.append(int(converter[part2[x]]) * (1 / target ** (x+1)))

#         return sum(nums1 + nums2)
#     else:
#         num = num[::-1]
#         for i in range(len(num)):
#             nums1.append(int(converter[num[i]]) * (target ** i))
        
#     return sum(nums1 + nums2)
# Failed. ???????????????

def hw2_try2(num, b, target): # works from 2 to 35 Position systems and converts all to decimal
    num = str(num)
    nums1 = []
    nums2 = []
    if "." in num:
        num = num.split(".")
        part1 = num[0][::-1]
        part2 = num[1]

        for i in range(len(part1)):
            nums1.append(int(converter[part1[i]]) * (b ** i))

        for x in range(len(part2)):
            nums2.append(int(converter[part2[x]]) * (1 / b ** (x+1)))

        result = sum(nums1 + nums2)
    else:
        num = num[::-1]
        for i in range(len(num)):
            nums1.append(int(converter[num[i]]) * (b ** i))

        result = sum(nums1)
    
    res = ""

    while int(result) != 0:
        res += str(int(result) % target)
        result = str(int(result) // target)

    return res[::-1]
# ✔

# ალგორითმი ნასწავლი და განხილულია homework.png'ში
# test:
print(hw2_try1(1001, 2)) # 9
print(hw2_try1(1001, 4)) # 65
print(hw2_try1(520.3, 10)) # 520.3
print(hw2_try1(1001, 16)) # 4097
print(hw2_try1(1011, 16)) # 4113
print(hw2_try1("1FFF", 16)) # 8191
print(hw2_try1("FFF", 16)) # 4095
print(hw2_try1(520.3, 6)) # 192.5
print()
print(hw2_try2(1001, 2, 4)) # 9
print(hw2_try2(1001, 4, 10)) # 65
print(hw2_try2(520.3, 10, 10)) # 520.3
print(hw2_try2(1001, 16, 10)) # 4097
print(hw2_try2(1011, 16, 10)) # 4113
print(hw2_try2("1FFF", 16, 10)) # 8191
print(hw2_try2("FFF", 16, 10)) # 4095
print(hw2_try2(520.3, 6, 10)) # 192.5

# print(hw2_try2(1001, 2, 10)) # 9
# print(hw2_try2(1001, 4, 12)) # 65
# print(hw2_try2(520.3, 10)) # 520.3
# print(hw2_try2(1001, 16)) # 4097
# print(hw2_try2(1011, 16)) # 4113
# print(hw2_try2("1FFF", 16)) # 8191
# print(hw2_try2("FFF", 16)) # 4095
# print(hw2_try2(520.3, 6)) # 192.5
