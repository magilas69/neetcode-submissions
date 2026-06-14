class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False
        first = {}
        second = {}

        for i in s:
            if (i not in first):
                first[i] = 1
            first[i] += 1
        for j in t:
            if (j not in second):
                second[j] = 1
            second[j] += 1
        if (first == second):
            return True
        return False
