class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a nested for loop i, j where j checks for days in the future
        # and sees if a temp is greater than i
        # time: O(n^2) space: O(N)

        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res
        