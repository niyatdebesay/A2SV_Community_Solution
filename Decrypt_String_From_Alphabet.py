class Solution:
    def freqAlphabets(self, s: str) -> str:
        final = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])  
                final.append(chr(num + 96))  
                i += 3  
            else:
                   
                num = int(s[i])  
                final.append(chr(num + 96))  
                i += 1  
        return ''.join(final)