def searchMatrix(matrix, target):
    if not matrix: return False
    if not matrix[0]: return False
    if target < matrix[0][0] or target > matrix[-1][-1]: return False
    row = len(matrix)  # 行
    col = len(matrix[0])  # 列
    for i in range(row):
        if matrix[i][-1] < target:
            continue
        for j in range(col):
            if matrix[i][j] == target:
                return True
        return False
