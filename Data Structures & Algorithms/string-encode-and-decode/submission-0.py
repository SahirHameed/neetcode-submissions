class Solution:

    def encode(self, strs: List[str]) -> str:
        # Ex: 4#ne#t4#code4#love4#you
        res = ''
        for s in strs:
            # res.join([str(len(s)), '#', s])
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # Loop first to get the length of the string
        # Then loop to add the string to the list
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
        

            