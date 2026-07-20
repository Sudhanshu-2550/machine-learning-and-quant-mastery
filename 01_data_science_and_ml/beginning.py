# 1. Beginning with Data Science and Machine Learning   
from ast import List


print("Welcome to the world of Data Science and Machine Learning!  SUDHANSHU")
#2. Creating variables (storing data)
name = "SUDHANSHU"
age = 19
height = 5.9
print(f"\ndeveloper name is {name}, age is {age} and height is {height} feet")
# 3. Doing some basics
daily_learning_hours = 11
days_in_a_week = 7
weekly_learning_hours = daily_learning_hours * days_in_a_week
print(f"\nWeekly learning hours: {weekly_learning_hours}")
#Leet code question 1 TWO SUM
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
#Leet code question 217 Contains duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4, 5]))
print(solution.containsDuplicate([1, 2, 3, 4, 3, 1]))