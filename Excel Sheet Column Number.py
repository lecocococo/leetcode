class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dict = {}
        cnt = 1
        
        for i in range(26):
            dict[chr(65 + i)] = i+1
            
        # print(dict)
        
        result = 0
        i = 0
        for ch in columnTitle[::-1]:
            result+=(math.pow(26,i))*dict[ch]
            i+=1
            
        return int(result)
