#!/usr/bin/python3

'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle

# def pascal_triangle(n):
#     '''Creates a list of lists of integers representing
#     the Pascal's triangle of a given integer.
#     '''
#     if type(n) is not int or n <= 0:
#         return []

#     triangle = [[1]]
#     while len(triangle) < n:
#         prev_row = triangle[-1]
#         new_row = [1]

#         for i in range(1, len(prev_row)):
#             new_row.append(prev_row[i-1] + prev_row[i])

#         new_row.append(1)
#         triangle.append(new_row)
    

#     return triangle

# result = pascal_triangle(5)
# for row in result:
#     print(row)

