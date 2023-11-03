"""
Problem Description:
    Given an integer, convert it to a roman numeral. Input is guaranteed to be
    within the range from 1 to 3999.

    Example 1:
        Input: 3
        Output: "III"

    Example 2:
        Input: 4
        Output: "IV"

"""
# Solution:
class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }

        # Result Variable
        r = ''

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n
        return r


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3))
    print(solution.intToRoman(4))
    print(solution.intToRoman(9))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))