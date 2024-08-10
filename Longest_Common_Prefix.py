class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for strings in strs[1:]:
            while not strings.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix