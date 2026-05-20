class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5,5#HelloWorld
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        
        res = ""
        for num in sizes:
            res += num + ","
        res += "#"
        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        # Size = [5,5]
        # res = []
        # i = 0
        size, res, i = [], [], 0
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            size.append(int(cur))
            i+=1
        i += 1
        for sz in size:
            res.append(s[i:i+sz])
            i += sz
        
        return res


