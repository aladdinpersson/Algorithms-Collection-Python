"""
O(n^2) algorithm, can be faster and done in O(nlogn), but this works ok.
To do: Create extensive test cases before adding to algorithm list.

"""


def longest_increasing_subsequence(nums):
    if len(nums) == 0:
        return 0

    OPT = [1 for i in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i] and OPT[j] + 1 > OPT[i]:
                OPT[i] = OPT[j] + 1

    return max(OPT)


if __name__ == "__main__":
    # test1 = [1,5,-2,10, 50, -10, 10, 1,2,3,4]
    test2 = [10, 1, 2, 11, 3, 5]
    # test3 = [10,9,8,5,3,2,1,2,3]
    # test4 = [1,5,2,3,4,5,6]
    test5 = []

    print(test2)
    print(longest_increasing_subsequence(test2))
