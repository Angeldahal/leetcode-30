# Problem Description:
# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines;
# otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
# Note:
# You may assume that both strings contain only lowercase letters.
# Examples:
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        canConstruct = True

        for alpha in ransomNote:
            if alpha not in magazine:
                canConstruct = False
                return canConstruct
            else:
                magazine = magazine.replace(alpha, "", 1)

        return canConstruct


# Solution 2: using dictionary
class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        # Create a dictionary to store character counts
        dictionary = {}

        # Iterate through the magazine and count characters
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        # Iterate through the ransom note and check character counts
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False

        return True



# Using the Solution
solution = Solution()
print(solution.canConstruct("ab", "acab"))

solution2 = Solution2()
print(solution2.canConstruct("ab", "acab"))