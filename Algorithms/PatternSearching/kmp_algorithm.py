class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        m = len(needle)
        n = len(haystack)
        lps = [0] * m
        # Creating long prefix sum array of the given pattern
        i = 1
        l = 0
        while i < m:
            if needle[i] == needle[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        # Searching for the pattern and returning the first index of matching pattern
        i = 0
        j = 0
        while j < n:
            print(needle[i], haystack[j])
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                if i > 0:
                    i = lps[i - 1]
                else:
                    j += 1
                # j += 1
            if i >= m:
                return j - m

        return -1

obj = Solution()

print(obj.strStr("mississippi","issip"))