class Solution:

    def encode(self, strs: List[str]) -> str:
        # Store the length of the string, a delimeter '#', and then the string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Ex: 5#Hello5#World

        res = []
        i = 0

        while i != len(s):
            j = i
            length = ""
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return res
