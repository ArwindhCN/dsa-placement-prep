# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy | Topic: Strings
# Key idea: loop i up to the longer length; append word1[i] / word2[i] only if i is in range;
#           collect in a list and "".join() once at the end.


class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        len1, len2 = len(word1), len(word2)

        # Iterate up to the length of the longer string
        for i in range(max(len1, len2)):
            if i < len1:
                result.append(word1[i])
            if i < len2:
                result.append(word2[i])

        return "".join(result)


# Time:  O(m + n)  - why: loop runs max(m, n) times; join touches every character once
# Space: O(m + n)  - why: the result list (the output)
