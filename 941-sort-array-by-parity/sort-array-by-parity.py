class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                result.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2 !=0:
                result.append(nums[i])
        return result

