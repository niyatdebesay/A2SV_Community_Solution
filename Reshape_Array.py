import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_array = np.array(mat)
        row = len(mat)
        column= len(mat[0])
        if r*c == row*column:
            return  mat_array.reshape(r, c)
        else:
            return mat