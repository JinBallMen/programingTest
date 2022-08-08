#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # enumerate → indexと要素を取得できる
        for index1, item1 in enumerate(nums) :
            for index2, item2 in enumerate(nums) :
                sum = 0
                if index1 != index2 :
                    sum = item1 + item2
                    if sum == target :
                        return [index1 , index2]

        
# @lc code=end

