# Problem Description:
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
#
# Examples:
#
#     pattern = "abba", str = "dog cat cat dog" should return true.
#     pattern = "abba", str = "dog cat cat fish" should return false.
#     pattern = "aaaa", str = "dog cat cat dog" should return false.
#     pattern = "abba", str = "dog dog dog dog" should return false.
#
# Solution:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}

        s_list = s.split(" ")

        if len(s_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dictionary:
                dictionary[pattern[i]] = s_list[i]
            elif dictionary[pattern[i]] != s_list[i]:
                return False

        common_value = []

        for key, value in dictionary.items():
            if value in common_value:
                return False
            else:
                common_value.append(value)

        return True


# TestCases:
if __name__ == "__main__":
    test = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(test.wordPattern(pattern, s))
    pattern = "abba"
    s = "dog cat cat fish"
    print(test.wordPattern(pattern, s))
    pattern = "aaaa"
    s = "dog cat cat dog"
    print(test.wordPattern(pattern, s))
    pattern = "abba"
    s = "dog dog dog dog"
    print(test.wordPattern(pattern, s))
