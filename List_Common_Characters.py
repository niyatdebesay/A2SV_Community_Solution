from collections import Counter
from typing import List
class Solution:
    
    def commonChars(self, words: List[str]) -> List[str]:
        
            common_count = Counter(words[0])
            for word in words[1:]:
                current_count = Counter(word)
                common_count &= current_count
            result = []
            for char, count in common_count.items():
                result.extend([char] * count)
            
            return result