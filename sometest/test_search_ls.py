def NumberSearch(target, matrix):
    if not matrix:return False
    if target < matrix[0][0] or target > matrix[-1][-1]:return False
    rw = len(matrix)
    cl = len(matrix[0])
    row = 0
    col = cl - 1
    while row < rw and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
    return False