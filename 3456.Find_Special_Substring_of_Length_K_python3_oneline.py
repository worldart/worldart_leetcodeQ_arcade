#4ms 23.33%RT

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        return any(len(list(grp)) == k for _, grp in groupby(s))
