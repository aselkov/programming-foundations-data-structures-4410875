# Tuples are immutable array-like structures

point = (5, 2)

x = point[0]
y = point[1]
# print(f"({x}, {y})")

def calculate_square_properties(side_length):
  area = side_length ** 2
  perimeter = side_length * 4
  return (area, perimeter)

result = calculate_square_properties(5)
print(f"Area: {result[0]}\r\nPerimeter:", result[1])