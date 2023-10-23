"""
Problem Description:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
Example:
    Input: "()"
    Output: true
    Input: "()[]{}"
    Output: true
    Input: "(]"
    Output: false
    Input: "([)]"
    Output: false

"""


class Solution:
    def isValid(self, s: str) -> bool:
        temp_list = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                temp_list.append(i)
            elif i == ")" or i == "}" or i == "]":
                try:
                    character = temp_list.pop()
                    if i == ")" and character == "(":
                        continue
                    elif i == "}" and character == "{":
                        continue
                    elif i == "]" and character == "[":
                        continue
                    else:
                        return False
                except:
                    return False

        return temp_list == []


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("{[]}"))
    print(solution.isValid("]"))
    print(solution.isValid("(("))
    print(solution.isValid("){"))
