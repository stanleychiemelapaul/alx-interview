#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)
    
    result = pascal_triangle(n)
    for row in result:
        print(row)

    return triangle

# Example usage:


# if __name__ == "__main__":
#     print_triangle(pascal_triangle(5))