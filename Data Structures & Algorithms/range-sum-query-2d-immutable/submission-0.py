class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums=0
        while row1<=row2:
            x=col1
            while x<=col2:
                sums+=self.matrix[row1][x]
                x+=1
            row1+=1
        return sums


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)