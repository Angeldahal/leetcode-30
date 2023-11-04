"""
Problem Description:
    Given a string s of words delimited by spaces, reverse the order of words.

    Example:
        Input: "hello world here"
        Output: "here world hello"

        Input: "   These needs to     be reversed   "
        Output: "reversed be to needs These"
"""


# Solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseList(listOfWords):
            reversedList = []
            for i in range(len(listOfWords)):
                reversedList.append(listOfWords[- i - 1])
            return reversedList

        s = " ".join(s.split())
        s_list = s.split(" ")
        s_list = reverseList(s_list)
        return " ".join(s_list)


# Sample Testcase:
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("hello world here"))
    print(solution.reverseWords("   These needs to     be reversed   "))
