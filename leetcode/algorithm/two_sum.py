"""
Author: Ted
Date: 2018/4/4
Description:
"""


class Solution(object):


    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_for = {}
        results = set()

        for n, x in enumerate(nums):
            try:
                results.add((look_for[x] + 1, n + 1))
            except KeyError:
                look_for.setdefault(target - x, n)
        return results


    @classmethod
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        look_for = {}
        results = set()

        for n, x in enumerate(nums):
            try:
                results.add((look_for[x], x))
            except KeyError:
                look_for.setdefault(target - x, x)
        return results


if __name__ == "__main__":
    # nums = list(range(10))
    nums = [1, 2, 3, 5, 50, 4]
    target = 7
    print("arrs: {0}\ntarget: {1}\nresulotion: {2}".format(nums, target, Solution.twoSum(nums=nums, target=target)))
    print("arrs: {0}\ntarget: {1}\nresulotion: {2}".format(nums, target, Solution.twoSum2(nums=nums, target=target)))
