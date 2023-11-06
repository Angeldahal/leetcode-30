"""
Problem Description:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
"""
# Solution:
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("TOPINTERVIEWQUESTION", 4))
    print(solution.convert("PYTHONSOLUTION", 5))
    print(solution.convert("PYTHON", 1))