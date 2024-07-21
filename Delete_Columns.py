class Solution(object):
    def minDeletionSize(self, strs):
        sum = 0
        for column in range(len(strs[0])):
            col = [strs[row][column] for row in range(len(strs))]
            if col != sorted(col):
                sum += 1
        return sum