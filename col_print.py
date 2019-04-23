def grid(rows, cols, padding):
  max_num_len = len(str(rows**cols))
  return '\n'.join([
    ''.join(['{{:>{}}}'.format(max_num_len+padding).format((row+1)**(col+1))
             for col in range(cols)])
    for row in range(rows)
  ])

print(grid(5, 5, 3))
