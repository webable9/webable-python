# page_138 : 유효한 팰린드롬
import re

# 단순 해결 방법
def isPalindrome(s):
    return s == s[::-1]


s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# 두번때 해결 방법
class Solution:
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower() # 소문자로 변경
        s = re.sub('[^a-z0-9]', '', s) # 정규식으로 불필요한 문자 필터링

        return s == s[::-1]  # 역슬라이싱


solution = Solution()
s = "race a car"
ans = solution.isPalindrome2(s)

if ans:
    print("Yes")
else:
    print("No")
