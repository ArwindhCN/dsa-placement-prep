# Problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
# Difficulty: Easy | Topic: Strings
# Key idea: check every letter a-z appears in the sentence (or: len(set(sentence)) == 26).


class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for letter in alphabet:
            if letter not in sentence:
                return False

        return True


# Time:  O(n)  - why: 26 checks, each `in` scans the string (O(n)) -> 26n = O(n)
# Space: O(1)  - why: the alphabet is a fixed 26 letters
# Notes: shorter: len(set(sentence)) == 26. string.ascii_lowercase saves typing the alphabet.
