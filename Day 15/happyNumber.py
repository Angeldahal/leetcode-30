"""
Problem Description:
    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.
    Example 1:
        Input: n = 19
        Output: true
        Explanation:
            12 + 92 = 82
            82 + 22 = 68
            62 + 82 = 100
            12 + 02 + 02 = 1

"""
# Solution:
class Solution:
    def isHappy(self, n: int) -> bool:
        sums = []
        while (True):
            sum = 0
            for i in str(n):
                sum += (int(i)) ** 2

            if sum == 1:
                return True

            if sum in sums:
                return False
            else:
                sums.append(sum)
                n = sum


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))
    print(solution.isHappy(2))
    print(solution.isHappy(7))
    print(solution.isHappy(1111111))
    print(solution.isHappy(11111111))
    print(solution.isHappy(111111111))
    print(solution.isHappy(1111111111))
    print(solution.isHappy(11111111111))
    print(solution.isHappy(111111111111))
    print(solution.isHappy(1111111111111))
    print(solution.isHappy(11111111111111))
    print(solution.isHappy(111111111111111))
    print(solution.isHappy(1111111111111111))
    print(solution.isHappy(11111111111111111))
    print(solution.isHappy(111111111111111111))
    print(solution.isHappy(1111111111111111111))
    print(solution.isHappy(11111111111111111111))
    print(solution.isHappy(111111111111111111111))
    print(solution.isHappy(1111111111111111111111))
    print(solution.isHappy(11111111111111111111111))
    print(solution.isHappy(111111111111111111111111))
    print(solution.isHappy(1111111111111111111111111))
    print(solution.isHappy(11111111111111111111111111))
    print(solution.isHappy(111111111111111111111111111))
    print(solution.isHappy(1111111111111111111111111111))
    print(solution.isHappy(11111111111111111111111111111))