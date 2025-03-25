class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers and their indices
        num_map = {}        
        for i, num in enumerate(nums):
            # Calculate the complement that would sum with num to reach the target
            complement = target - num            
            # Check if the complement is already in the dictionary
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices of the complement and current number
            # Store the number and its index in the dictionary
            num_map[num] = i
        
        return None  # Return None if no solution is found
