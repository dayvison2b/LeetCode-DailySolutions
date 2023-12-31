# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():
            result.append(word[::-1])
        return " ".join(result)
    
    
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
    
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        for word in s.split():
            result = result + " " + word[::-1]
        return result[1:]
    
    
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split()))