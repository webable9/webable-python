# page_145 : 문자열 뒤집기
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s


solution = Solution()

s = ["h", "e", "l", "l", "o"]
ans = solution.reverseString(s)

print(ans)
