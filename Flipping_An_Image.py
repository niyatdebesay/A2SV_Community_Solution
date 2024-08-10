from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        listlen = len(image[0])
        for i in range(len(image)):
            image[i].reverse()
            for e in range(listlen):
                if image[i][e] == 0:
                    image[i][e]=1
                else:
                    image[i][e]=0
        return image